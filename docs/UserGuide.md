# User Guide

**Project:** PDF Merger  
**Project ID:** 007  
**Version:** 1.0.0

---

# Table of Contents

1. Introduction
2. System Requirements
3. Installing the Application
4. Launching the Application
5. User Interface Overview
6. Merging PDF Files
7. Error Messages
8. Frequently Asked Questions (FAQ)
9. Troubleshooting
10. Current Limitations
11. Future Enhancements
12. Version History

---

# 1. Introduction

PDF Merger is a Windows desktop application that combines multiple PDF documents into a single PDF file.

The application is designed to provide a simple and efficient way to organize multiple PDF documents while preserving the original page quality, page orientation, and page order.

Version 1.0 focuses on providing a reliable PDF merging utility with a clean and intuitive interface.

---

# 2. System Requirements

## Operating System

- Windows 10 or later

## Software Requirements

- Python 3.14 (when running from source)

or

- Standalone executable (.exe)

## Disk Space

Less than 100 MB

---

# 3. Installing the Application

## Running from Source

### Step 1

Download or clone the project.

### Step 2

Install the required dependencies.

```bash
pip install -r requirements.txt
```

### Step 3

Launch the application.

```bash
python main.py
```

---

## Running the Executable

If using the packaged version:

1. Open the **dist** folder.
2. Double-click **PDF Merger.exe**.
3. The application will start.

No Python installation is required when using the executable.

---

# 4. Launching the Application

After launching the application, the main window will appear.

The interface consists of:

- File List
- Action Buttons
- Status Bar

Initially no PDF files are loaded.

The Merge button remains disabled until PDF files are selected.

---

# 5. User Interface Overview

## File List

Displays all selected PDF files.

Information shown includes:

- File Name
- Page Count
- File Size

---

## Action Panel

### Add PDFs

Allows selection of one or more PDF files.

---

### Merge PDFs

Combines the selected PDF files into one output document.

---

## Status Bar

Displays application status such as:

- Ready
- PDF files loaded
- Merge completed

---

# 6. Merging PDF Files

## Step 1

Click **Add PDFs**.

---

## Step 2

Select one or more PDF files.

Multiple files may be selected at once.

---

## Step 3

The selected PDFs appear in the file list.

Verify that the required documents are displayed.

---

## Step 4

Click **Merge PDFs**.

---

## Step 5

Choose:

- Output folder
- Output file name

---

## Step 6

Click **Save**.

The application merges the selected PDF files.

---

## Step 7

A success message is displayed after completion.

The merged PDF is saved to the selected location.

---

# 7. Error Messages

## No PDF Selected

**Message**

> Please select one or more PDF files.

---

## Invalid File

**Message**

> Only PDF files are supported.

---

## Invalid Output File

**Message**

> Please specify an output file.

---

## Merge Failed

**Message**

> Unable to merge the selected PDF files.

Possible reasons include:

- Corrupted PDF
- Password-protected PDF
- File permission issues

---

# 8. Frequently Asked Questions (FAQ)

## Does the application modify my original PDF files?

No.

The original PDF files remain unchanged.

---

## Is page quality reduced?

No.

The application preserves the original document quality.

---

## Will landscape pages be converted to portrait?

No.

Landscape pages remain landscape.

Portrait pages remain portrait.

---

## Can I merge password-protected PDFs?

Not in Version 1.0.

---

## Is an internet connection required?

No.

The application runs entirely on your local computer.

---

# 9. Troubleshooting

## The Merge button is disabled

Ensure that at least one PDF has been added.

---

## The application cannot open a PDF

Verify that:

- The file exists.
- The PDF is not corrupted.
- The PDF is not password protected.

---

## Unable to save the merged PDF

Check that:

- The destination folder exists.
- You have write permission.
- The output file is not open in another application.

---

# 10. Current Limitations

Version 1.0 intentionally focuses on core PDF merging functionality.

The following features are not currently available:

- Remove selected PDF
- Reorder PDF files
- Drag and drop
- PDF thumbnails
- Page rotation
- Page deletion
- Merge selected pages
- Password support
- Bookmark editing
- Metadata editing

These features are planned for future releases.

---

# 11. Future Enhancements

Planned improvements include:

- Drag and drop support
- Remove selected PDF
- Reorder PDF files
- Merge selected page ranges
- Page rotation
- Thumbnail previews
- Password support
- Bookmark preservation
- Metadata editor
- Recent files list

---

# 12. Version History

| Version | Description |
|----------|-------------|
| 1.0.0 | Initial release |

---

**End of User Guide**