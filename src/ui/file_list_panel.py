"""
Project : PDF Merger
Project ID : 007

File List Panel
"""

import customtkinter as ctk

from src.models.pdf_file import PDFFile
from src.utils.format_utils import format_file_size


class FileListPanel(ctk.CTkFrame):
    """
    Displays the list of loaded PDF files.
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self._create_widgets()

    def _create_widgets(self) -> None:
        """
        Creates the panel widgets.
        """
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="Selected PDF Files",
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.title_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="ew",
        )

        self.file_listbox = ctk.CTkTextbox(
            self,
            state="disabled",
            wrap="none",
        )
        self.file_listbox.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10),
            sticky="nsew",
        )

    def load_files(self, pdf_files: list[PDFFile]) -> None:
        """
        Displays the loaded PDF files.
        """
        self.clear()

        self.file_listbox.configure(state="normal")

        for index, pdf in enumerate(pdf_files, start=1):
            line = (
                f"{index:>2}. "
                f"{pdf.file_name}\n"
                f"     Pages : {pdf.page_count}\n"
                f"     Size  : {format_file_size(pdf.file_size)}\n\n"
            )

            self.file_listbox.insert("end", line)

        self.file_listbox.configure(state="disabled")

    def clear(self) -> None:
        """
        Clears the displayed file list.
        """
        self.file_listbox.configure(state="normal")
        self.file_listbox.delete("1.0", "end")
        self.file_listbox.configure(state="disabled")