"""
Project : PDF Merger
Project ID : 007

PDF Merger
"""

from pathlib import Path

from src.core.validation import Validation
from src.models.merge_result import MergeResult
from src.models.pdf_file import PDFFile
from src.services.pdf_service import PDFService


class PDFMerger:
    """
    Coordinates the PDF merge workflow.
    """

    def __init__(self) -> None:
        self._pdf_files: list[PDFFile] = []

    @property
    def pdf_files(self) -> list[PDFFile]:
        """
        Returns the currently loaded PDF files.
        """
        return self._pdf_files

    def add_pdf(self, pdf_file: PDFFile) -> None:
        """
        Adds a single PDF.

        Args:
            pdf_file: PDF to add.
        """
        self._pdf_files.append(pdf_file)

    def add_pdfs(self, pdf_files: list[PDFFile]) -> None:
        """
        Adds multiple PDFs.

        Args:
            pdf_files: List of PDF files.
        """
        self._pdf_files.extend(pdf_files)

    def clear(self) -> None:
        """
        Removes all loaded PDFs.
        """
        self._pdf_files.clear()

    def has_files(self) -> bool:
        """
        Returns True if one or more PDFs are loaded.
        """
        return len(self._pdf_files) > 0

    def get_pdf_count(self) -> int:
        """
        Returns the number of loaded PDFs.
        """
        return len(self._pdf_files)

    def merge(self, output_path: Path) -> MergeResult:
        """
        Merges the loaded PDF files.

        Args:
            output_path: Destination PDF path.

        Returns:
            MergeResult describing the outcome.
        """
        is_valid, message = Validation.validate_merge(
            self._pdf_files,
            output_path,
        )

        if not is_valid:
            return MergeResult(
                success=False,
                message=message,
            )

        try:
            PDFService.merge_pdfs(
                self._pdf_files,
                output_path,
            )

            return MergeResult(
                success=True,
                message="PDFs merged successfully.",
                output_file=output_path,
            )

        except Exception as error:
            return MergeResult(
                success=False,
                message=str(error),
            )