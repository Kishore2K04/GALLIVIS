from collections import Counter
from pathlib import Path

import imagehash
from PIL import Image

from app.config.dataset_config import (
    SUPPORTED_IMAGE_EXTENSIONS,
    ULTRASOUND_RAW_DIR,
)


def get_image_files() -> list[Path]:
    """Return all supported image files in the ultrasound dataset."""

    return [
        path
        for path in ULTRASOUND_RAW_DIR.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
    ]


def analyze_images() -> dict:
    """Analyze dimensions, formats, and perceptual hashes."""

    files = get_image_files()

    dimensions = Counter()
    formats = Counter()
    hashes = {}

    corrupted = []

    for file_path in files:
        try:
            with Image.open(file_path) as image:
                image.verify()

            with Image.open(file_path) as image:
                dimensions[image.size] += 1
                formats[image.format] += 1
                hashes[str(file_path)] = str(imagehash.phash(image))

        except Exception:
            corrupted.append(str(file_path))

    hash_groups = {}

    for file_path, file_hash in hashes.items():
        hash_groups.setdefault(file_hash, []).append(file_path)

    duplicates = {
        file_hash: paths
        for file_hash, paths in hash_groups.items()
        if len(paths) > 1
    }

    return {
        "total_images": len(files),
        "dimensions": dimensions,
        "formats": formats,
        "corrupted": corrupted,
        "duplicates": duplicates,
    }