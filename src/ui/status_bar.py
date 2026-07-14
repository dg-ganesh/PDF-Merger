"""
Project : PDF Merger
Project ID : 007

Status Bar
"""

import customtkinter as ctk

from src.config import (
    STATUS_COMPLETED,
    STATUS_MERGING,
    STATUS_READY,
)


class StatusBar(ctk.CTkFrame):
    """
    Displays application status messages.
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self._create_widgets()
        self.show_ready()

    def _create_widgets(self) -> None:
        """
        Creates the status bar.
        """
        self.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            anchor="w",
        )

        self.status_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="ew",
        )

    def set_status(self, message: str) -> None:
        """
        Updates the displayed status message.

        Args:
            message: Status text.
        """
        self.status_label.configure(text=message)

    def show_ready(self) -> None:
        """
        Displays the default ready status.
        """
        self.set_status(STATUS_READY)

    def show_merging(self) -> None:
        """
        Displays the merge-in-progress status.
        """
        self.set_status(STATUS_MERGING)

    def show_completed(self) -> None:
        """
        Displays the merge completed status.
        """
        self.set_status(STATUS_COMPLETED)

    def show_files_loaded(self, count: int) -> None:
        """
        Displays the number of loaded PDF files.

        Args:
            count: Number of loaded PDFs.
        """
        self.set_status(f"{count} PDF file(s) loaded.")