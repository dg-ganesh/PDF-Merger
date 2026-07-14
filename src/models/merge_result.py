"""
Project : PDF Merger
Project ID : 007

Merge Result Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class MergeResult:
    """
    Represents the result of a PDF merge operation.
    """

    success: bool
    message: str
    output_file: Path | None = None

    @property
    def output_file_name(self) -> str:
        """
        Returns the output file name.
        """
        if self.output_file is None:
            return ""

        return self.output_file.name

    @property
    def output_directory(self) -> Path | None:
        """
        Returns the directory containing the merged PDF.
        """
        if self.output_file is None:
            return None

        return self.output_file.parent

    @property
    def has_output_file(self) -> bool:
        """
        Indicates whether an output file was created.
        """
        return self.output_file is not None