import os

def display_menu():
    print("\n\tNote Taking App")
    print("1. View Note")
    print("2. Add Note")
    print("3. Delete Note")
    print("4. Exit")

def delete_note():
    print("Exiting Notes: ")
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        print("No notes available")
        return

    for i,filename in enumerate(os.listdir(notes_dir)):
        with open(os.path.join(notes_dir,filename),"r") as file:
            content = file.read()
            print(f"{i}.{filename[:-4]}: {content[:-10]}")


    note_no = input("Which one you want to delete? Enter the title: ")
    note_path = os.path.join(notes_dir, f"{note_no}.txt")
    if os.path.exists(note_path):
        os.remove(note_path)
    else:
        print("Note is not available...")

def view_note():
    print("\nExiting Notes: ")
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        print("No notes available")
        return
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir, filename), 'r') as file:
            content = file.read()
            print(f"{filename[:-4]}: {content}")

            
def add_note():
    note_title = input("Enter the Note Title: ")
    note_content = input("Note Content: ")
    note_dir = 'notes'
    if not os.path.exists(note_dir):
        os.makedirs(note_dir)
    note_path = os.path.join(note_dir, f"{note_title}.txt")

    with open (note_path, 'a') as file:
        file.write(f"{note_content}\n")
    print(f"Note '{note_title}' Taken successfully....")


def main():
    while True:
        display_menu()
        num = int(input("Enter you choice: "))
        if num == 1:
            view_note()
        elif num == 2:
            add_note()
        elif num == 3:
            delete_note()
        elif num == 4:
            exit()
        else:
            print("Enter the right choice..")

if __name__=="__main__":
    main()