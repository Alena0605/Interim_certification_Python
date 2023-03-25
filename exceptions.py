from datetime import datetime as dt


def input_data():
    title = check_title()
    text = check_text("Add some description")
    date = dt.now().strftime('%Y-%m-%d %A %H:%M')

    return [title, text, date]


def check_title():
    title = input("Enter the title (press enter to pass): ")
    if not title:
        title = "NO TITLE"

    return title


def check_text(msg):
    while True:
        text = input(f"{msg} (enter 'q' to cancel): ")
        if text == 'q' or text == 'Q':
            text = ''
        elif not text:
            print("The note can't be empty!")

        return text


def check_note(notes_list):
    if type(notes_list) is list:
        while True:
            id = check_input("Enter the ID of the note")

            for note in notes_list:
                if id == int(note[1]):
                    return note

            print("ERROR! Note not found! Try again.")


def check_input(msg):
    while True:
        try:
            number = int(input(f"{msg}: "))
            return number
        except ValueError:
            print('-' * 50)
            print("Incorrect input! It's not a number!")
