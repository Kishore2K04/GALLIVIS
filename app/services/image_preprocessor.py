from pathlib import Path

from PIL import Image
import numpy as np


TARGET_SIZE = (224, 224)


def preprocess_image(
    input_path: Path,
    output_path: Path,
) -> None:
    """
    Preprocess one ultrasound image.

    The original image is never modified.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with Image.open(input_path) as image:

        # Convert to RGB for consistent CNN input
        image = image.convert("RGB")

        # Resize to CNN input size
        image = image.resize(
            TARGET_SIZE,
            Image.Resampling.LANCZOS,
        )

        # Convert to NumPy array
        array = np.asarray(image, dtype=np.float32)

        # Normalize pixel values from [0, 255] to [0, 1]
        array = array / 255.0

        # Convert back to image for storage
        processed_image = Image.fromarray(
            (array * 255).astype(np.uint8)
        )

        processed_image.save(
            output_path,
            format="JPEG",
            quality=95,
        )