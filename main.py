# Simple Notes Taking App

from datetime import datetime
from pathlib import Path

def main():
    """
    This function is the entry point of the Simple Notes Taking App.
    It allows the user to write notes and saves them to a file called "notes.txt".
    The function prompts the user for input until the user types "exit" to exit the app.
    """

    # Write Date
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Create Date Folder
    date_name = now.strftime("%d-%m-%Y")
    file_path = str(Path.cwd()) + "/notes/" + date_name + ".txt"

    with open(file_path, "a") as file:
        file.write("Note Date: " + dt_string + "\n")

    # Welcome Message
    print("Welcome to Simple Notes Taking App")

    # Enter the subject
    subject = input("Enter the subject: ")

    # Write Subject
    with open(file_path, "a") as file:
        file.write("Subject: " + subject + "\n")

    # Index
    index = 1

    # Take Notes
    while True:

        # Take Note
        note = input(f"{index}. ")

        # Exit
        if note == "exit" or note == "finished":
            break

        # Clear Notes
        elif note == "clear":
            with open(file_path, "w") as file:  
                file.write("")
            break

        # Reset Index
        elif note == "reset":
            main()
            break

        # Empty Note
        elif note == "":
            print("Please write something or type 'exit' to exit the app.")
            continue

        # Write Note
        else:
            # Write Note
            with open(file_path, "a") as file:
                file.write(f"{index}. {note}\n")

            # Increment Index
            index += 1

    return

if __name__ == "__main__":
    main()
