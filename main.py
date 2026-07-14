"""
Project : PDF Merger
Project ID : 007

Application Entry Point
"""

import customtkinter as ctk

from src.ui.main_window import MainWindow


def configure_application() -> None:
    """
    Configures application-wide settings.
    """
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")


def main() -> None:
    """
    Creates and starts the application.
    """
    configure_application()

    application = MainWindow()
    application.run()


if __name__ == "__main__":
    main()