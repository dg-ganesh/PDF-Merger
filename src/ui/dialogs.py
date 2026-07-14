"""
Project : PDF Merger
Project ID : 007

Dialogs
"""

from tkinter import messagebox


class Dialogs:
    """
    Provides common application dialog boxes.
    """

    @staticmethod
    def show_info(title: str, message: str) -> None:
        """
        Displays an information dialog.

        Args:
            title: Dialog title.
            message: Dialog message.
        """
        messagebox.showinfo(
            title=title,
            message=message,
        )

    @staticmethod
    def show_warning(title: str, message: str) -> None:
        """
        Displays a warning dialog.

        Args:
            title: Dialog title.
            message: Dialog message.
        """
        messagebox.showwarning(
            title=title,
            message=message,
        )

    @staticmethod
    def show_error(title: str, message: str) -> None:
        """
        Displays an error dialog.

        Args:
            title: Dialog title.
            message: Dialog message.
        """
        messagebox.showerror(
            title=title,
            message=message,
        )

    @staticmethod
    def show_success(title: str, message: str) -> None:
        """
        Displays a success dialog.

        Args:
            title: Dialog title.
            message: Dialog message.
        """
        messagebox.showinfo(
            title=title,
            message=message,
        )

    @staticmethod
    def confirm(title: str, message: str) -> bool:
        """
        Displays a confirmation dialog.

        Args:
            title: Dialog title.
            message: Dialog message.

        Returns:
            True if the user selects Yes; otherwise False.
        """
        return messagebox.askyesno(
            title=title,
            message=message,
        )