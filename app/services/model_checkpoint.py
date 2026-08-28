from pathlib import Path

import torch
import torch.nn as nn


def save_model(
    model: nn.Module,
    output_path: Path,
) -> None:

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    torch.save(
        model.state_dict(),
        output_path,
    )


def model_exists(
    model_path: Path,
) -> bool:

    return model_path.is_file()