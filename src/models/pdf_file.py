"""
Project : PDF Merger
Project ID : 007

PDF File Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PDFFile:
    """
    Represents a PDF document selected by the user.
    """

    file_path: Path
    page_count: int
    file_size: int

    @property
    def file_name(self) -> str:
        """
        Returns the file name including extension.
        """
        return self.file_path.name

    @property
    def file_extension(self) -> str:
        """
        Returns the file extension.
        """
        return self.file_path.suffix.lower()

    @property
    def parent_folder(self) -> Path:
        """
        Returns the parent folder of the PDF.
        """
        return self.file_path.parent

    @property
    def file_size_kb(self) -> float:
        """
        Returns the file size in KB.
        """
        return round(self.file_size / 1024, 2)

    @property
    def file_size_mb(self) -> float:
        """
        Returns the file size in MB.
        """
        return round(self.file_size / (1024 * 1024), 2)