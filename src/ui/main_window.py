"""
Project : PDF Merger
Project ID : 007

Main Window
"""

import customtkinter as ctk

from src.config import (
    MIN_WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    PROJECT_NAME,
    STATUS_COMPLETED,
    STATUS_READY,
)
from src.core.pdf_merger import PDFMerger
from src.services.file_service import FileService
from src.services.pdf_service import PDFService
from src.ui.action_panel import ActionPanel
from src.ui.dialogs import Dialogs
from src.ui.file_list_panel import FileListPanel
from src.ui.status_bar import StatusBar


class MainWindow(ctk.CTk):
    """
    Main application window.
    """

    def __init__(self) -> None:
        super().__init__()

        self.pdf_merger = PDFMerger()

        self._configure_window()
        self._create_widgets()
        self._wire_events()

    def _configure_window(self) -> None:
        """
        Configures the application window.
        """
        self.title(PROJECT_NAME)
        self.geometry("900x600")
        self.minsize(
            MIN_WINDOW_WIDTH,
            MIN_WINDOW_HEIGHT,
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def _create_widgets(self) -> None:
        """
        Creates the UI.
        """
        self.file_list_panel = FileListPanel(self)
        self.file_list_panel.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=10,
            sticky="nsew",
        )

        self.action_panel = ActionPanel(self)
        self.action_panel.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=10,
            sticky="ns",
        )

        self.action_panel.disable_merge()

        self.status_bar = StatusBar(self)
        self.status_bar.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
        )

    def _wire_events(self) -> None:
        """
        Connects button events.
        """
        self.action_panel.set_add_command(self.add_pdfs)
        self.action_panel.set_merge_command(self.merge_pdfs)

    def add_pdfs(self) -> None:
        """
        Loads PDF files.
        """
        paths = FileService.select_pdf_files()

        if not paths:
            return

        self.pdf_merger.clear()

        pdf_files = []

        for path in paths:
            pdf = PDFService.load_pdf(path)
            pdf_files.append(pdf)

        self.pdf_merger.add_pdfs(pdf_files)

        self.file_list_panel.load_files(
            self.pdf_merger.pdf_files
        )

        self.status_bar.set_status(
            f"{self.pdf_merger.get_pdf_count()} PDF(s) loaded."
        )

        self.action_panel.enable_merge()

    def merge_pdfs(self) -> None:
        """
        Merges the loaded PDFs.
        """
        output_file = FileService.select_output_file()

        if output_file is None:
            return

        result = self.pdf_merger.merge(output_file)

        if result.success:
            self.status_bar.set_status(
                STATUS_COMPLETED
            )

            Dialogs.show_success(
                "Success",
                result.message,
            )

        else:
            Dialogs.show_error(
                "Error",
                result.message,
            )

            self.status_bar.set_status(
                STATUS_READY
            )

    def run(self) -> None:
        """
        Starts the application.
        """
        self.mainloop()