def view_notes():
    with open("notes.txt", "r") as file:
        print(file.read())

view_notes()

