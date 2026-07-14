"""
Project : PDF Merger
Project ID : 007

Application Configuration
"""

from pathlib import Path

# =============================================================================
# Application Information
# =============================================================================

PROJECT_ID = "007"
PROJECT_NAME = "PDF Merger"
APP_VERSION = "1.0.0"

# =============================================================================
# Window Configuration
# =============================================================================

WINDOW_TITLE = PROJECT_NAME

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

MIN_WINDOW_WIDTH = 700
MIN_WINDOW_HEIGHT = 500

# =============================================================================
# Supported File Types
# =============================================================================

SUPPORTED_EXTENSIONS = [".pdf"]

PDF_FILE_FILTER = (
    ("PDF Files", "*.pdf"),
    ("All Files", "*.*"),
)

# =============================================================================
# Default Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
SAMPLES_DIR = DATA_DIR / "samples"

# =============================================================================
# Default Output
# =============================================================================

DEFAULT_OUTPUT_FILENAME = "Merged.pdf"

# =============================================================================
# Status Messages
# =============================================================================

STATUS_READY = "Ready"

STATUS_FILES_LOADED = "PDF file(s) loaded."

STATUS_MERGING = "Merging PDF files..."

STATUS_COMPLETED = "Merge completed successfully."

# =============================================================================
# Dialog Titles
# =============================================================================

INFO_TITLE = "Information"

WARNING_TITLE = "Warning"

ERROR_TITLE = "Error"

SUCCESS_TITLE = "Success"

# =============================================================================
# Validation Messages
# =============================================================================

MSG_NO_FILES_SELECTED = "Please select one or more PDF files."

MSG_INVALID_FILE = "Only PDF files are supported."

MSG_OUTPUT_REQUIRED = "Please specify an output file."

MSG_FILE_ALREADY_EXISTS = (
    "The selected output file already exists. "
    "Do you want to replace it?"
)

MSG_MERGE_SUCCESS = "PDF files merged successfully."

MSG_MERGE_FAILED = "Unable to merge the selected PDF files."

# =============================================================================
# Application Limits
# =============================================================================

MAX_RECENT_FILES = 10