import csv
from pathlib import Path

from PIL import Image

from app.config.dataset_config import (
    ULTRASOUND_RAW_DIR,
    ULTRASOUND_PROCESSED_DIR,
    METADATA_DIR,
)


def generate_metadata():
    """Generate metadata for all ultrasound images."""

    METADATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = METADATA_DIR / "ultrasound_metadata.csv"

    image_files = [
        path
        for path in ULTRASOUND_RAW_DIR.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
    ]

    with output_file.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "image_id",
            "patient_id",
            "image_path",
            "processed_path",
            "width",
            "height",
            "format",
            "composition_label",
            "label_source",
        ])

        for index, image_path in enumerate(
            sorted(image_files),
            start=1,
        ):

            relative_path = image_path.relative_to(
                ULTRASOUND_RAW_DIR
            )

            processed_path = (
                ULTRASOUND_PROCESSED_DIR
                / relative_path
            )

            with Image.open(image_path) as image:
                width, height = image.size
                image_format = image.format

            writer.writerow([
                f"US_{index:05d}",
                "",
                str(relative_path),
                str(processed_path.relative_to(
                    ULTRASOUND_PROCESSED_DIR
                )),
                width,
                height,
                image_format,
                "",
                "",
            ])

    print(f"Metadata created: {output_file}")
    print(f"Images recorded: {len(image_files)}")


if __name__ == "__main__":
    generate_metadata()