from pathlib import Path

from app.config.settings import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    BASE_DIR,
)


METADATA_DIR = BASE_DIR / "data" / "metadata"

ULTRASOUND_RAW_DIR = RAW_DATA_DIR / "ultrasound"
CLINICAL_RAW_DIR = RAW_DATA_DIR / "clinical"
SPECTROSCOPY_RAW_DIR = RAW_DATA_DIR / "spectroscopy"

ULTRASOUND_PROCESSED_DIR = PROCESSED_DATA_DIR / "ultrasound"
CLINICAL_PROCESSED_DIR = PROCESSED_DATA_DIR / "clinical"

SUPPORTED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
}

GALLSTONE_CLASSES = [
    "cholesterol",
    "pigment",
    "mixed",
]