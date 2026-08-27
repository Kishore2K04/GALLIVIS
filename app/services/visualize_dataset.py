from pathlib import Path

import matplotlib.pyplot as plt

from app.config.dataset_config import (
    ULTRASOUND_PROCESSED_DIR,
)


def main():

    image_files = sorted(
        ULTRASOUND_PROCESSED_DIR.rglob("*.jpg")
    )

    if not image_files:
        print("No processed images found.")
        return

    # Select a few images for inspection.
    selected = image_files[:9]

    for image_path in selected:

        image = plt.imread(image_path)

        plt.figure(figsize=(6, 5))
        plt.imshow(image)
        plt.title(image_path.name)
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    main()