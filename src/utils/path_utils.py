"""
Project : PDF Merger
Project ID : 007

Path Utilities
"""

from pathlib import Path

from src.config import SUPPORTED_EXTENSIONS


def is_pdf_file(file_path: Path) -> bool:
    """
    Returns True if the file has a supported PDF extension.
    """
    return file_path.suffix.lower() in SUPPORTED_EXTENSIONS


def file_exists(file_path: Path) -> bool:
    """
    Returns True if the file exists.
    """
    return file_path.exists() and file_path.is_file()


def directory_exists(directory: Path) -> bool:
    """
    Returns True if the directory exists.
    """
    return directory.exists() and directory.is_dir()


def ensure_pdf_extension(file_path: Path) -> Path:
    """
    Ensures the supplied path has a .pdf extension.
    """
    if file_path.suffix.lower() == ".pdf":
        return file_path

    return file_path.with_suffix(".pdf")


def is_same_file(file_one: Path, file_two: Path) -> bool:
    """
    Returns True if both paths refer to the same file.
    """
    try:
        return file_one.resolve() == file_two.resolve()
    except OSError:
        return False


def get_file_size(file_path: Path) -> int:
    """
    Returns the file size in bytes.
    """
    return file_path.stat().st_size