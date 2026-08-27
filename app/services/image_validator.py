from pathlib import Path

from PIL import Image

from app.config.dataset_config import SUPPORTED_IMAGE_EXTENSIONS


def is_supported_extension(file_path: Path) -> bool:
    """Check whether the image uses a supported file extension."""

    return file_path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS


def is_valid_image(file_path: Path) -> bool:
    """Check whether an image can be opened and verified."""

    if not file_path.exists():
        return False

    if not is_supported_extension(file_path):
        return False

    try:
        with Image.open(file_path) as image:
            image.verify()

        return True

    except Exception:
        return False