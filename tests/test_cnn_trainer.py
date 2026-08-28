import torch
from torch.utils.data import DataLoader, TensorDataset

from app.models.cnn_classifier import GallivisCNN
from app.services.cnn_trainer import train_model


def test_training_engine():

    # Small synthetic dataset.
    # This is ONLY to test the training code.
    images = torch.randn(12, 3, 224, 224)

    labels = torch.tensor([
        0, 1, 2,
        0, 1, 2,
        0, 1, 2,
        0, 1, 2,
    ])

    dataset = TensorDataset(images, labels)

    train_loader = DataLoader(
        dataset,
        batch_size=4,
        shuffle=True,
    )

    validation_loader = DataLoader(
        dataset,
        batch_size=4,
        shuffle=False,
    )

    model = GallivisCNN()

    trained_model, history = train_model(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        epochs=1,
        learning_rate=0.001,
    )

    assert trained_model is not None

    assert len(history) == 1

    assert "train_loss" in history[0]
    assert "train_accuracy" in history[0]
    assert "validation_loss" in history[0]
    assert "validation_accuracy" in history[0]