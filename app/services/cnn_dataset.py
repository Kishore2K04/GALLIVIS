import csv
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import Dataset


CLASS_NAMES = {
    "Cholesterol": 0,
    "Pigment": 1,
    "Mixed": 2,
}


class GallivisUltrasoundDataset(Dataset):
    """
    PyTorch dataset for GALLIVIS ultrasound images.

    Only images with verified composition labels are accepted.
    """

    def __init__(
        self,
        metadata_path: Path,
        image_root: Path,
    ):
        self.metadata_path = Path(metadata_path)
        self.image_root = Path(image_root)

        self.records = self._load_records()

        if not self.records:
            raise ValueError(
                "No labelled ultrasound images found. "
                "Verified Cholesterol/Pigment/Mixed labels are required."
            )

    def _load_records(self) -> list[dict]:
        records = []

        with self.metadata_path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                label = row["composition_label"].strip()

                # Ignore currently unlabeled images.
                if not label:
                    continue

                if label not in CLASS_NAMES:
                    raise ValueError(
                        f"Unknown composition label: {label}"
                    )

                records.append(row)

        return records

    def __len__(self) -> int:
        return len(self.records)

    def __getitem__(self, index: int):
        record = self.records[index]

        image_path = self.image_root / record["processed_path"]

        image = Image.open(image_path).convert("RGB")

        # Convert image to tensor in [0, 1].
        image_tensor = torch.from_numpy(
            __import__("numpy").array(image)
        ).float() / 255.0

        # HWC -> CHW
        image_tensor = image_tensor.permute(2, 0, 1)

        label = CLASS_NAMES[
            record["composition_label"].strip()
        ]

        return image_tensor, torch.tensor(
            label,
            dtype=torch.long,
        )