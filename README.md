# Python File Management System

A simple command-line File Management System built using Python. This project demonstrates basic file handling operations using Python's built-in modules.

## Features

- **Create Files** — Create new files and write content to them.
- **Read Files** — Read and display the contents of existing files.
- **Update Files** — Rename files, overwrite existing content, or append new content.
- **Delete Files** — Remove files from the system.
- **File Listing** — Display files and folders using recursive path searching.
- **Error Handling** — Handle common errors using `try-except` blocks.

## Technologies Used

- Python
- `pathlib` — Path and file-system operations
- `os` — File deletion operations
- File handling with `open()`, `read()`, and `write()`
- Exception handling with `try-except`

## Project Structure

```text
python-file-management-system/
│
├── main.py
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/guptaxaditya55/python-file-management-system.git
```

### 2. Navigate to the Project Directory

```bash
cd python-file-management-system
```

### 3. Run the Program

```bash
python main.py
```

If your system uses the Python launcher on Windows, you can also run:

```powershell
py main.py
```

## How to Use

After running the program, select an operation from the menu:

1. Create a file
2. Read a file
3. Update a file
4. Delete a file

Follow the prompts to enter the filename and perform the selected operation.

## Learning Objectives

Through this project, I practised:

- Defining and calling Python functions
- Working with loops and conditional statements
- Using `pathlib.Path` to check file paths
- Reading and writing files with context managers (`with open()`)
- Understanding file modes: `r`, `w`, and `a`
- Handling exceptions
- Using Git and GitHub for version control

## Future Improvements

- Add a continuous menu using a `while` loop
- Improve input validation and error messages
- Add file search by name and extension
- Add confirmation before deleting files
- Organize the project into separate modules
- Add automated tests

## Author

**Aditya Prakash**

GitHub: [@guptaxaditya55](https://github.com/guptaxaditya55)

---

This project was created as part of my Python learning journey to strengthen my understanding of file handling and filesystem operations.`