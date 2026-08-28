from pathlib import Path

from app.services.dataset_split import split_dataset


def test_dataset_split():

    image_paths = [
        Path(f"image_{i}.jpg")
        for i in range(30)
    ]

    labels = (
        [0] * 10
        + [1] * 10
        + [2] * 10
    )

    (
        train_paths,
        train_labels,
        validation_paths,
        validation_labels,
        test_paths,
        test_labels,
    ) = split_dataset(
        image_paths,
        labels,
    )

    assert len(train_paths) == 21
    assert len(validation_paths) == 4
    assert len(test_paths) == 5

    assert len(train_labels) == 21
    assert len(validation_labels) == 4
    assert len(test_labels) == 5

    assert len(
        set(train_paths)
        & set(validation_paths)
    ) == 0

    assert len(
        set(train_paths)
        & set(test_paths)
    ) == 0

    assert len(
        set(validation_paths)
        & set(test_paths)
    ) == 0