# 📝 Simple Notes App

A lightweight **Command-Line Interface (CLI) Notes Management Application** built with Python.

The Simple Notes App allows users to **create, view, search, and delete notes** directly from the terminal. Notes are automatically stored in a text file, so your data remains available even after the program is closed.

---

## ✨ Features

* ➕ **Add Notes** — Create and save new text notes.
* 👀 **View Notes** — Display all saved notes with their index numbers.
* 🔍 **Search Notes** — Search notes using keywords with case-insensitive matching.
* 🗑️ **Delete Notes** — Remove notes safely using their index number.
* 💾 **Automatic Persistence** — Notes are automatically saved to `notes.txt`.
* ⚠️ **Input Validation** — Prevents empty notes and handles invalid inputs.
* 🧩 **Modular Structure** — Functionality is separated into independent Python modules.

---

## 📁 Project Structure

```text
simple-notes-app/
│
├── main.py        # Application entry point and main control loop
├── menu.py        # Displays the application menu
├── notes.py       # Core note operations
├── storage.py     # Handles reading and writing notes
├── notes.txt      # Stores saved notes (automatically created)
└── README.md      # Project documentation
```

### Module Responsibilities

| File         | Responsibility                                |
| ------------ | --------------------------------------------- |
| `main.py`    | Runs the application and handles user choices |
| `menu.py`    | Displays the CLI menu                         |
| `notes.py`   | Adds, views, searches, and deletes notes      |
| `storage.py` | Saves and loads notes from the text file      |
| `notes.txt`  | Persistent storage for notes                  |

---

## 🛠️ Technologies Used

* **Python 3.x**
* **File Handling**
* **Lists & Strings**
* **Functions**
* **Exception Handling**
* **Command-Line Interface (CLI)**

No external Python libraries are required.

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.x is installed on your system.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## ▶️ Running the Application

### 1. Download or clone the project

Place all project files inside the same directory.

### 2. Open the terminal

Navigate to the project directory:

```bash
cd simple-notes-app
```

### 3. Run the application

```bash
python main.py
```

---

## 💻 Usage

After starting the application, you will see:

```text
========== NOTES APP ==========

1. Add note
2. View notes
3. Delete note
4. Search notes
5. Exit

===============================
Choose (1-5):
```

### 1️⃣ Add Note

Choose `1` and enter the text of your note.

```text
Choose (1-5): 1

Write your note:
> Complete Python project

Note saved!
```

Empty notes are rejected automatically.

---

### 2️⃣ View Notes

Choose `2` to display all saved notes.

```text
Choose (1-5): 2

Your Notes:
1. Complete Python project
2. Study for calculus
3. Submit assignment
```

Each note is assigned an index number for easy management.

---

### 3️⃣ Delete Note

Choose `3` and enter the index of the note you want to remove.

```text
Choose (1-5): 3

Your Notes:
1. Complete Python project
2. Study for calculus
3. Submit assignment

Enter note number to delete: 2

Note deleted successfully!
```

Invalid note numbers are handled without crashing the application.

---

### 4️⃣ Search Notes

Choose `4` and enter a keyword.

```text
Choose (1-5): 4

Enter keyword: python

Search results:
1. Complete Python project
```

The search is **case-insensitive**, so `Python`, `python`, and `PYTHON` can all find the same note.

---

### 5️⃣ Exit

Choose `5` to safely close the application.

```text
Choose (1-5): 5

Goodbye!
```

Your notes remain stored in `notes.txt`.

---

## 💾 Data Storage

The application uses a simple text file named:

```text
notes.txt
```

The file is automatically created when notes are saved.

This approach keeps the project lightweight and avoids requiring a database.

---

## 🧠 Concepts Demonstrated

This project demonstrates several fundamental Python programming concepts:

* Functions and modular programming
* Lists and string manipulation
* Conditional statements
* Loops
* User input handling
* File reading and writing
* Exception handling
* Input validation
* Searching and indexing
* Separation of responsibilities between modules

---

## 🔄 Application Flow

```text
          ┌──────────────┐
          │   Start App  │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │ Load Notes   │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │ Display Menu │
          └──────┬───────┘
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      Add      View    Search
        │        │        │
        └────────┼────────┘
                 │
              Delete
                 │
                 ▼
          ┌──────────────┐
          │ Save Changes │
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │     Exit     │
          └──────────────┘
```

---

## 🔮 Future Improvements

Possible upgrades for future versions include:

* 📅 Add timestamps to notes
* ✏️ Edit existing notes
* 🏷️ Add categories or tags
* ⭐ Mark important notes
* 🔐 Add password protection
* 📊 Store notes using SQLite
* 🎨 Add a better terminal interface
* ☁️ Add cloud synchronization
* 📤 Export notes to PDF or other formats

---

## 🎯 Project Objective

The main objective of this project is to build a simple but practical Python application while demonstrating **modular programming, file handling, user input validation, and persistent data storage**.

---

## 👨‍💻 Author

**Adhithya Chakravarthi D**

**B.Tech CSE Core — VIT Bhopal University**

**Project:** Simple Notes App

---

## 📄 License

This project was created for **educational and academic purposes**.
