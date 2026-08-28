from pathlib import Path

import torch
import torch.nn.functional as F
from PIL import Image

from app.models.cnn_classifier import GallivisCNN


CLASS_NAMES = [
    "Cholesterol",
    "Pigment",
    "Mixed",
]

IMAGE_SIZE = (224, 224)


def load_model(
    model_path: Path,
    device: torch.device | None = None,
) -> tuple[GallivisCNN, torch.device]:

    if device is None:
        device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

    model = GallivisCNN(num_classes=3)

    checkpoint = torch.load(
        model_path,
        map_location=device,
    )

    model.load_state_dict(checkpoint)

    model.to(device)
    model.eval()

    return model, device


def preprocess_for_inference(
    image_path: Path,
) -> torch.Tensor:

    image = Image.open(image_path).convert("RGB")

    image = image.resize(
        IMAGE_SIZE,
        Image.Resampling.LANCZOS,
    )

    image_tensor = torch.from_numpy(
        __import__("numpy").array(image)
    ).float() / 255.0

    image_tensor = image_tensor.permute(2, 0, 1)

    # Add batch dimension.
    image_tensor = image_tensor.unsqueeze(0)

    return image_tensor


@torch.no_grad()
def predict(
    model: GallivisCNN,
    image_path: Path,
    device: torch.device,
) -> dict:

    image_tensor = preprocess_for_inference(
        image_path
    ).to(device)

    logits = model(image_tensor)

    probabilities = F.softmax(
        logits,
        dim=1,
    )[0]

    predicted_index = int(
        torch.argmax(probabilities).item()
    )

    confidence = float(
        probabilities[predicted_index].item()
    )

    return {
        "prediction": CLASS_NAMES[predicted_index],
        "confidence": confidence,
        "probabilities": {
            CLASS_NAMES[index]: float(
                probabilities[index].item()
            )
            for index in range(len(CLASS_NAMES))
        },
    }