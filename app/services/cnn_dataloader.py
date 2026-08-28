from pathlib import Path

from torch.utils.data import DataLoader

from app.services.cnn_dataset import (
    GallivisUltrasoundDataset,
)


def create_dataloader(
    metadata_path: Path,
    image_root: Path,
    batch_size: int = 16,
    shuffle: bool = True,
) -> DataLoader:

    dataset = GallivisUltrasoundDataset(
        metadata_path=metadata_path,
        image_root=image_root,
    )

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=0,
    )