import csv

import pytest

from app.services.cnn_dataset import (
    GallivisUltrasoundDataset,
)


def test_unlabeled_dataset_is_rejected(tmp_path):

    metadata_path = tmp_path / "metadata.csv"

    with metadata_path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:

        writer = csv.writer(file)

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

        writer.writerow([
            "US_00001",
            "",
            "test.jpg",
            "test.jpg",
            "1200",
            "900",
            "JPEG",
            "",
            "",
        ])

    with pytest.raises(ValueError):
        GallivisUltrasoundDataset(
            metadata_path,
            tmp_path,
        )