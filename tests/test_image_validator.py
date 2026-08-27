from pathlib import Path

from app.services.image_validator import is_supported_extension


def test_supported_jpg_extension():
    assert is_supported_extension(Path("test.jpg")) is True


def test_supported_png_extension():
    assert is_supported_extension(Path("test.png")) is True


def test_unsupported_extension():
    assert is_supported_extension(Path("test.txt")) is False