from pathlib import Path

from app.config.dataset_config import ULTRASOUND_RAW_DIR
from app.services.image_validator import is_valid_image


def scan_ultrasound_directory() -> dict:
    """Scan the ultrasound directory and summarize available images."""

    total_files = 0
    valid_images = 0
    invalid_images = []

    for file_path in ULTRASOUND_RAW_DIR.rglob("*"):

        if not file_path.is_file():
            continue

        total_files += 1

        if is_valid_image(file_path):
            valid_images += 1
        else:
            invalid_images.append(str(file_path))

    return {
        "directory": str(ULTRASOUND_RAW_DIR),
        "total_files": total_files,
        "valid_images": valid_images,
        "invalid_images": invalid_images,
    }