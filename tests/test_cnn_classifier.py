import torch

from app.models.cnn_classifier import GallivisCNN


def test_model_creation():
    model = GallivisCNN()

    assert model is not None


def test_model_output_shape():
    model = GallivisCNN()

    sample_input = torch.randn(2, 3, 224, 224)

    output = model(sample_input)

    assert output.shape == (2, 3)