View Notes Function

A beginner-friendly Python project that demonstrates how to read and display notes from a text file using functions.

📌 Description

This program:

Creates a function named view_notes()
Opens a file called notes.txt
Reads all saved notes from the file
Prints the file content on the screen

The program uses with open() which automatically closes the file after reading.

🧠 Concepts Used

Functions
File Handling
with open()
Read Mode ('r')
read() method
print() function

💻 Code

def view_notes():
    with open("notes.txt", "r") as file:
        print(file.read())

view_notes()

▶️ Example Output

Hello
Learn Python daily
