"""
Project : PDF Merger
Project ID : 007

PDF Service
"""

from pathlib import Path

from pypdf import PdfReader, PdfWriter

from src.models.pdf_file import PDFFile


class PDFService:
    """
    Service responsible for PDF operations.
    """

    @staticmethod
    def load_pdf(file_path: Path) -> PDFFile:
        """
        Loads a PDF and returns its metadata.

        Args:
            file_path: Path to the PDF file.

        Returns:
            PDFFile object.
        """
        reader = PdfReader(file_path)

        return PDFFile(
            file_path=file_path,
            page_count=len(reader.pages),
            file_size=file_path.stat().st_size,
        )

    @staticmethod
    def merge_pdfs(pdf_files: list[PDFFile], output_file: Path) -> None:
        """
        Merges multiple PDF files into a single PDF.

        Args:
            pdf_files: Ordered list of PDFFile objects.
            output_file: Destination PDF path.
        """
        writer = PdfWriter()

        for pdf in pdf_files:
            reader = PdfReader(pdf.file_path)

            for page in reader.pages:
                writer.add_page(page)

        with output_file.open("wb") as file:
            writer.write(file)

    @staticmethod
    def get_page_count(file_path: Path) -> int:
        """
        Returns the number of pages in a PDF.

        Args:
            file_path: Path to the PDF.

        Returns:
            Page count.
        """
        reader = PdfReader(file_path)
        return len(reader.pages)

    @staticmethod
    def is_password_protected(file_path: Path) -> bool:
        """
        Checks whether a PDF is password protected.

        Args:
            file_path: Path to the PDF.

        Returns:
            True if the PDF is encrypted.
        """
        reader = PdfReader(file_path)
        return reader.is_encrypted