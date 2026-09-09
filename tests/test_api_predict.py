import io

from fastapi.testclient import TestClient
from PIL import Image

import app.main as main_module
from app.main import app
from app.models.cnn_classifier import GallivisCNN
from app.services.model_checkpoint import save_model


client = TestClient(app)


def _make_dummy_jpeg_bytes() -> bytes:
    image = Image.new("RGB", (224, 224), color=(120, 120, 120))
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    return buffer.getvalue()


def test_predict_rejects_non_image_upload():

    response = client.post(
        "/predict/ultrasound",
        files={"file": ("notes.txt", b"not an image", "text/plain")},
    )

    assert response.status_code == 400


def test_predict_returns_503_when_no_checkpoint_exists(tmp_path, monkeypatch):

    missing_checkpoint = tmp_path / "no_such_model.pt"

    monkeypatch.setattr(main_module, "CHECKPOINT_PATH", missing_checkpoint)
    monkeypatch.setattr(main_module, "_model", None)
    monkeypatch.setattr(main_module, "_device", None)

    response = client.post(
        "/predict/ultrasound",
        files={"file": ("scan.jpg", _make_dummy_jpeg_bytes(), "image/jpeg")},
    )

    assert response.status_code == 503
    assert "No trained GALLIVIS model checkpoint" in response.json()["detail"]


def test_predict_returns_valid_schema_with_untrained_checkpoint(tmp_path, monkeypatch):
    """
    This only verifies that the API <-> CNN wiring works end-to-end.
    The checkpoint here is a randomly-initialized model saved purely
    for this test. It carries no medical meaning and makes no
    accuracy claim whatsoever.
    """

    dummy_checkpoint = tmp_path / "dummy_model.pt"
    save_model(GallivisCNN(), dummy_checkpoint)

    monkeypatch.setattr(main_module, "CHECKPOINT_PATH", dummy_checkpoint)
    monkeypatch.setattr(main_module, "_model", None)
    monkeypatch.setattr(main_module, "_device", None)

    response = client.post(
        "/predict/ultrasound",
        files={"file": ("scan.jpg", _make_dummy_jpeg_bytes(), "image/jpeg")},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["prediction"] in ("Cholesterol", "Pigment", "Mixed")
    assert 0.0 <= body["confidence"] <= 1.0
    assert set(body["probabilities"].keys()) == {
        "Cholesterol",
        "Pigment",
        "Mixed",
    }
    assert abs(sum(body["probabilities"].values()) - 1.0) < 1e-4
    assert "decision support" in body["disclaimer"]