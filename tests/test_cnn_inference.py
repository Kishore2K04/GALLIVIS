import torch

from app.models.cnn_classifier import GallivisCNN
from app.services.cnn_inference import (
    CLASS_NAMES,
)


def test_class_names():

    assert CLASS_NAMES == [
        "Cholesterol",
        "Pigment",
        "Mixed",
    ]


def test_softmax_probabilities():

    model = GallivisCNN()

    logits = torch.tensor(
        [[1.0, 2.0, 3.0]]
    )

    probabilities = torch.softmax(
        logits,
        dim=1,
    )

    assert probabilities.shape == (1, 3)

    assert torch.isclose(
        probabilities.sum(),
        torch.tensor(1.0),
    )

    predicted_index = int(
        probabilities.argmax(dim=1).item()
    )

    assert predicted_index == 2