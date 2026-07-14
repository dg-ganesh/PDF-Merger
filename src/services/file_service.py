"""
Project : PDF Merger
Project ID : 007

File Service
"""

from pathlib import Path
from tkinter import Tk, filedialog


class FileService:
    """
    Service responsible for file and folder selection.
    """

    @staticmethod
    def select_pdf_files() -> list[Path]:
        """
        Opens a file selection dialog for PDF files.

        Returns:
            List of selected PDF file paths.
        """
        root = Tk()
        root.withdraw()

        file_paths = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*"),
            ],
        )

        root.destroy()

        return [Path(path) for path in file_paths]

    @staticmethod
    def select_output_file(default_name: str = "Merged.pdf") -> Path | None:
        """
        Opens a Save As dialog for the merged PDF.

        Args:
            default_name: Suggested output filename.

        Returns:
            Output file path or None if cancelled.
        """
        root = Tk()
        root.withdraw()

        file_path = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            initialfile=default_name,
            filetypes=[
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*"),
            ],
        )

        root.destroy()

        if not file_path:
            return None

        return Path(file_path)

    @staticmethod
    def select_output_folder() -> Path | None:
        """
        Opens a folder selection dialog.

        Returns:
            Selected folder path or None if cancelled.
        """
        root = Tk()
        root.withdraw()

        folder = filedialog.askdirectory(
            title="Select Output Folder"
        )

        root.destroy()

        if not folder:
            return None

        return Path(folder)