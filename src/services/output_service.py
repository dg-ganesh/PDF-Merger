"""
Project : PDF Merger
Project ID : 007

Output Service
"""

from pathlib import Path

from src.config import DEFAULT_OUTPUT_FILENAME
from src.utils.path_utils import ensure_pdf_extension


class OutputService:
    """
    Service responsible for output file preparation and validation.
    """

    @staticmethod
    def get_default_output_name() -> str:
        """
        Returns the default output filename.
        """
        return DEFAULT_OUTPUT_FILENAME

    @staticmethod
    def prepare_output_path(output_path: Path) -> Path:
        """
        Ensures the output path has a PDF extension.

        Args:
            output_path: Selected output path.

        Returns:
            Validated output path.
        """
        return ensure_pdf_extension(output_path)

    @staticmethod
    def output_exists(output_path: Path) -> bool:
        """
        Checks whether the output file already exists.

        Args:
            output_path: Output PDF path.

        Returns:
            True if the file already exists.
        """
        return output_path.exists()

    @staticmethod
    def parent_directory_exists(output_path: Path) -> bool:
        """
        Checks whether the destination directory exists.

        Args:
            output_path: Output PDF path.

        Returns:
            True if the parent directory exists.
        """
        return output_path.parent.exists()

    @staticmethod
    def is_writable(output_path: Path) -> bool:
        """
        Checks whether the destination directory is writable.

        Args:
            output_path: Output PDF path.

        Returns:
            True if the directory is writable.
        """
        try:
            test_file = output_path.parent / ".write_test"

            with test_file.open("w", encoding="utf-8"):
                pass

            test_file.unlink()

            return True

        except (PermissionError, OSError):
            return False