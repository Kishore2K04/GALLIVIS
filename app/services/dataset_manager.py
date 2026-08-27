from pathlib import Path

from app.config.dataset_config import (
    ULTRASOUND_RAW_DIR,
    CLINICAL_RAW_DIR,
    SPECTROSCOPY_RAW_DIR,
)


def get_data_directories() -> dict[str, Path]:
    """Return the official GALLIVIS data directories."""

    return {
        "ultrasound": ULTRASOUND_RAW_DIR,
        "clinical": CLINICAL_RAW_DIR,
        "spectroscopy": SPECTROSCOPY_RAW_DIR,
    }


def verify_data_directories() -> dict[str, bool]:
    """Verify that all required data directories exist."""

    directories = get_data_directories()

    return {
        name: path.exists()
        for name, path in directories.items()
    }


if __name__ == "__main__":
    print("GALLIVIS Data Directories")
    print("=" * 40)

    for name, exists in verify_data_directories().items():
        status = "OK" if exists else "MISSING"
        print(f"{name}: {status}")