import os



def view_note():
    print("Existing Notes: ")
    note_dir = "notes1"
    if not os.path.exists(note_dir):
        print("There is no note exists... Thank you!!!")

    for filename in os.listdir(note_dir):
        with open(os.path.join(note_dir, filename), "r") as file:
            content  = file.read()
            print(f"{filename}: {content[:-4]}")


def take_note():
    note_title= input("Enter your note title: ")
    note_details = input("Enter your note: ")
    note_dir = "notes1"

    if not os.path.exists(note_dir):
        os.makedirs(note_dir)

    note_path = os.path.join(note_dir, f"{note_title}.txt")

    with open(note_path, "a") as note:
        note.write(f"{note_details}\n")
    print(f"Note {note_title} write successfully")

