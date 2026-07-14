"""
Project : PDF Merger
Project ID : 007

Validation
"""

from pathlib import Path

from src.models.pdf_file import PDFFile
from src.services.output_service import OutputService


class Validation:
    """
    Performs validation for the PDF merge workflow.
    """

    @staticmethod
    def validate_pdf_list(pdf_files: list[PDFFile]) -> tuple[bool, str]:
        """
        Validates that at least one PDF has been selected.

        Args:
            pdf_files: List of selected PDF files.

        Returns:
            Tuple containing validation status and message.
        """
        if not pdf_files:
            return False, "Please select one or more PDF files."

        return True, ""

    @staticmethod
    def validate_output_path(output_path: Path | None) -> tuple[bool, str]:
        """
        Validates the output path.

        Args:
            output_path: Destination PDF path.

        Returns:
            Tuple containing validation status and message.
        """
        if output_path is None:
            return False, "Please specify an output file."

        if not OutputService.parent_directory_exists(output_path):
            return False, "The selected output folder does not exist."

        if not OutputService.is_writable(output_path):
            return False, "The selected output folder is not writable."

        return True, ""

    @staticmethod
    def validate_duplicate_files(
        pdf_files: list[PDFFile],
    ) -> tuple[bool, str]:
        """
        Checks for duplicate PDF selections.

        Args:
            pdf_files: List of selected PDF files.

        Returns:
            Tuple containing validation status and message.
        """
        file_paths = [pdf.file_path.resolve() for pdf in pdf_files]

        if len(file_paths) != len(set(file_paths)):
            return False, "Duplicate PDF files are not allowed."

        return True, ""

    @staticmethod
    def validate_merge(
        pdf_files: list[PDFFile],
        output_path: Path | None,
    ) -> tuple[bool, str]:
        """
        Performs all merge validations.

        Args:
            pdf_files: Selected PDF files.
            output_path: Destination PDF path.

        Returns:
            Tuple containing validation status and message.
        """
        is_valid, message = Validation.validate_pdf_list(pdf_files)
        if not is_valid:
            return False, message

        is_valid, message = Validation.validate_duplicate_files(pdf_files)
        if not is_valid:
            return False, message

        is_valid, message = Validation.validate_output_path(output_path)
        if not is_valid:
            return False, message

        return True, ""