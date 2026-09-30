3# Simple Notes App
from storage import open_notes
from notes import append_note, view_notes, delete_note, search_notes
from menu import show_menu

# Main program
notes = open_notes()

#using loops and nested if concepts 

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        append_note(notes)
    
    elif choice == "2":
        view_notes(notes)
    
    elif choice == "3":
        delete_note(notes)
    
    elif choice == "4":
        search_notes(notes)
    
    elif choice == "5":
        print("\nGoodbye!")
        break
    
    else:
        print("Wrong choice! Try again.")
