import hashlib
from collections import defaultdict
from pathlib import Path

from app.config.dataset_config import (
    SUPPORTED_IMAGE_EXTENSIONS,
    ULTRASOUND_RAW_DIR,
)


def calculate_sha256(file_path: Path) -> str:
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_exact_duplicates() -> dict[str, list[str]]:
    """Find files with exactly identical contents."""

    hashes = defaultdict(list)

    for file_path in ULTRASOUND_RAW_DIR.rglob("*"):

        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
            continue

        file_hash = calculate_sha256(file_path)

        hashes[file_hash].append(str(file_path))

    return {
        file_hash: paths
        for file_hash, paths in hashes.items()
        if len(paths) > 1
    }