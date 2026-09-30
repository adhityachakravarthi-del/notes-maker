Simple Notes App

A lightweight, command-line interface (CLI) notes management application written in Python. This program allows users to create, view, search, and delete text notes with automatic persistence using a plain text file.

Features

 Add Notes: Quick creation of new note entries with empty-string validation.

 View Notes: Indexed overview of all active notes.

 Search Notes: Case-insensitive keyword search across all stored notes.

 Delete Notes: Safe deletion of notes by index number with error handling.

 Automatic Persistence: Automatically saves and loads notes to and from notes.txt.

Project Structure

The codebase is organized into modular components:

simple-notes-app/
│
├── main.py        # Application entry point; handles the main control loop
├── menu.py        # UI component for displaying options
├── notes.py       # Core note functions (add, view, delete, search)
├── storage.py     # File I/O functions for reading and writing data
└── notes.txt      # Text file storing persistent note data (auto-generated)


How to Run

Prerequisites

Python 3.x installed on your machine.

Execution

Clone or download the repository files into the same directory.

Open your terminal or command prompt and navigate to the project directory.

Run the main entry file:

python main.py


Usage Guide

Upon running the application, you will be presented with a menu options list:

========== NOTES APP ==========
1. Add note
2. View notes
3. Delete note
4. Search notes
5. Exit
==============================
Choose (1-5):


Add Note: Select 1 and type your note text at the prompt.

View Notes: Select 2 to list all existing notes alongside their reference numbers.

Delete Note: Select 3, view your notes list, and enter the corresponding number to remove an entry.

Search Notes: Select 4 and enter a keyword to filter matching notes.

Exit: Select 5 to exit the program.
