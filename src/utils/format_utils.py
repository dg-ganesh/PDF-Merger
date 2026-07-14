"""
Project : PDF Merger
Project ID : 007

Format Utilities
"""


def format_file_size(file_size: int) -> str:
    """
    Converts a file size in bytes to a human-readable string.

    Args:
        file_size: File size in bytes.

    Returns:
        Human-readable file size.
    """
    units = ["Bytes", "KB", "MB", "GB", "TB"]

    size = float(file_size)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "Bytes":
                return f"{int(size)} {unit}"

            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} TB"


def format_page_count(page_count: int) -> str:
    """
    Returns a properly formatted page count string.

    Args:
        page_count: Number of pages.

    Returns:
        Formatted page count.
    """
    if page_count == 1:
        return "1 Page"

    return f"{page_count} Pages"