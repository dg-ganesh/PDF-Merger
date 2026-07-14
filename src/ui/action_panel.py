"""
Project : PDF Merger
Project ID : 007

Action Panel
"""

import customtkinter as ctk


class ActionPanel(ctk.CTkFrame):
    """
    Displays the primary application actions.
    """

    def __init__(self, master) -> None:
        super().__init__(master)

        self._create_widgets()

    def _create_widgets(self) -> None:
        """
        Creates the action buttons.
        """
        self.grid_columnconfigure(0, weight=1)

        self.add_button = ctk.CTkButton(
            self,
            text="Add PDFs",
        )
        self.add_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 10),
            sticky="ew",
        )

        self.merge_button = ctk.CTkButton(
            self,
            text="Merge PDFs",
        )
        self.merge_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=(10, 15),
            sticky="ew",
        )

    def set_add_command(self, command) -> None:
        """
        Assigns the Add PDFs button callback.
        """
        self.add_button.configure(command=command)

    def set_merge_command(self, command) -> None:
        """
        Assigns the Merge PDFs button callback.
        """
        self.merge_button.configure(command=command)

    def enable_merge(self) -> None:
        """
        Enables the Merge button.
        """
        self.merge_button.configure(state="normal")

    def disable_merge(self) -> None:
        """
        Disables the Merge button.
        """
        self.merge_button.configure(state="disabled")