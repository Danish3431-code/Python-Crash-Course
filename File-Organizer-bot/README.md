# 📁 File Organizer Bot

A lightweight Python script that automatically organizes files in a folder by sorting them into subfolders based on their file extension.

## Overview

Manually sorting through a cluttered folder (Downloads, Desktop, etc.) is tedious. This script scans a target directory and moves every file into a subfolder named after its extension — for example, all `.jpg` files go into a `jpg/` folder, all `.pdf` files go into a `pdf/` folder, and files with no extension go into a `No Extension/` folder.

## Features

- Automatically detects file extensions and creates matching folders
- Handles files with no extension gracefully
- Skips subfolders — only organizes files in the top-level directory
- Simple, dependency-free (uses only Python's standard library)
- Clear success/error messaging

## Requirements

- Python 3.x
- No external libraries required (`os` and `shutil` are built-in)

## How It Works

1. Prompts the user to enter a folder path.
2. Validates that the path exists; exits with an error message if not.
3. Lists all items in the folder and filters out anything that isn't a file (subfolders are skipped).
4. For each file, extracts its extension using `os.path.splitext()`.
5. Files without an extension are grouped into a folder named `No Extension`.
6. Creates a destination folder named after the extension if it doesn't already exist.
7. Moves the file into its matching extension folder using `shutil.move()`.
8. Prints a success message once all files are processed.

## Usage

1. Clone or download this repository.
2. Run the script:
```bash
   python file_organizer.py
```
3. When prompted, enter the full path of the folder you want to organize:4. The script will create subfolders (e.g., `pdf`, `jpg`, `txt`, `No Extension`) and move each file into the matching folder.
Downloads/
├── resume.pdf
├── photo.jpg
├── notes.txt
├── archive               
**After:** Downloads/
├── pdf/
│ └── resume.pdf
├── jpg/
│ └── photo.jpg
├── txt/
│ └── notes.txt
├── No Extension/
│ └── archive
├── photo.jpg
├── notes.txt
├── archive:**
## Known Limitations

- Does not scan subfolders recursively — only organizes files directly inside the given path.
- If a file with the same name already exists in the destination folder, behavior depends on the OS and may overwrite the existing file.
- Extensions are case-sensitive, so `.PDF` and `.pdf` will be treated as different types and placed in separate folders.

## Possible Improvements

- [ ] Normalize extensions to lowercase before creating folders
- [ ] Add a dry-run mode to preview changes before moving files
- [ ] Handle duplicate filenames instead of overwriting
- [ ] Add recursive organization for subfolders
- [ ] Add a simple GUI or drag-and-drop interface

## License

This project is open-source and free to use, modify, and distribute.

---

Built with Python 🐍
