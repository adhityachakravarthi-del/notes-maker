# Load notes from file
def open_notes():
    try:
        f = open("notes.txt", "r")
        all_notes = f.read().split("\n")
        f.close()
        return all_notes
    except:
        return []

# Save notes to file
def save_notes(notes):
    f = open("notes.txt", "w")
    f.write("\n".join(notes))
    f.close()
