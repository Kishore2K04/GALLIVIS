from pathlib import Path

from sklearn.model_selection import train_test_split


def split_dataset(
    image_paths: list[Path],
    labels: list[int],
    train_ratio: float = 0.70,
    validation_ratio: float = 0.15,
    test_ratio: float = 0.15,
    random_state: int = 42,
):
    """
    Split a labelled dataset into train, validation and test sets.
    """

    total = train_ratio + validation_ratio + test_ratio

    if abs(total - 1.0) > 1e-6:
        raise ValueError(
            "Train, validation and test ratios must sum to 1.0."
        )

    if len(image_paths) != len(labels):
        raise ValueError(
            "Number of images and labels must match."
        )

    train_paths, temp_paths, train_labels, temp_labels = (
        train_test_split(
            image_paths,
            labels,
            test_size=(validation_ratio + test_ratio),
            random_state=random_state,
            stratify=labels,
        )
    )

    relative_test_size = (
        test_ratio / (validation_ratio + test_ratio)
    )

    validation_paths, test_paths, validation_labels, test_labels = (
        train_test_split(
            temp_paths,
            temp_labels,
            test_size=relative_test_size,
            random_state=random_state,
            stratify=temp_labels,
        )
    )

    return (
        train_paths,
        train_labels,
        validation_paths,
        validation_labels,
        test_paths,
        test_labels,
    )