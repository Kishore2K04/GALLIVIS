from pathlib import Path

from app.config.dataset_config import (
    SUPPORTED_IMAGE_EXTENSIONS,
    ULTRASOUND_RAW_DIR,
    ULTRASOUND_PROCESSED_DIR,
)

from app.services.image_preprocessor import preprocess_image


def preprocess_dataset() -> tuple[int, int]:
    """Preprocess all ultrasound images."""

    processed = 0
    failed = 0

    image_files = [
        path
        for path in ULTRASOUND_RAW_DIR.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
    ]

    for input_path in image_files:

        relative_path = input_path.relative_to(
            ULTRASOUND_RAW_DIR
        )

        output_path = (
            ULTRASOUND_PROCESSED_DIR
            / relative_path
        )

        try:
            preprocess_image(
                input_path,
                output_path,
            )

            processed += 1

        except Exception as error:
            failed += 1

            print(
                f"Failed: {input_path}"
            )
            print(f"Reason: {error}")

    return processed, failed


def main():

    print("\nGALLIVIS Ultrasound Preprocessing")
    print("=" * 50)

    processed, failed = preprocess_dataset()

    print(f"\nProcessed images: {processed}")
    print(f"Failed images: {failed}")


if __name__ == "__main__":
    main()