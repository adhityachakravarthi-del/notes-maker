from storage import save_notes

# Add a new note
def append_note(notes):
    print("\nWrite your note:")
    note = input("> ")
    if note.strip():
        notes.append(note)
        save_notes(notes)
        print("Note saved!")
    else:
        print("Empty note!")

# View all notes
def view_notes(notes):
    print("\n--- Your Notes ---")
    if not notes or notes == ['']:
        print("No notes yet!")
        return
    
    for i in range(len(notes)):
        if notes[i].strip():
            print(str(i + 1) + ". " + notes[i])

# Delete a note
def delete_note(notes):
    view_notes(notes)
    print("\nDelete note (enter number):")
    try:
        num = int(input("> "))
        if 1 <= num <= len(notes):
            removed = notes.pop(num - 1)
            save_notes(notes)
            print("Deleted: " + removed)
        else:
            print("Wrong number!")
    except:
        print("Invalid!")

# Search notes
def search_notes(notes):
    word = input("Search for: ")
    print("\n--- Results ---")
    found = 0
    for i in range(len(notes)):
        if word.lower() in notes[i].lower():
            print(str(i + 1) + ". " + notes[i])
            found = found + 1
    
    if found == 0:
        print("No matches!")
