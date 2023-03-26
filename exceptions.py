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

    return title.upper()


def check_text(msg):
    while True:
        text = input(f"{msg} (enter 'q' to cancel): ")
        if text == 'q' or text == 'Q':
            text = ''
            return text
        elif not text:
            print("The note can't be empty!")
        else:
            return text


def check_note(notes_list):
    while True:
        id = check_input("Enter the ID of the note")

        for note in notes_list:
            if id == int(note[1]):
                return note

        print()
        print("ERROR! Note not found! Try again.\n")


def check_input(msg):
    while True:
        try:
            number = int(input(f"{msg}: "))
            return number
        except ValueError:
            print('=' * 50)
            print("Incorrect input! It's not a number!")
            print('=' * 50)


def check_chosen_note(notes_list, index, msg):
    while True:
        action = input(f"Enter 'yes' if you want to {msg} this note, or 'no' to refuse: ")
        if action.isalpha() and action.lower() == 'yes':
            notes_list.pop(index)
            return notes_list
        elif action.isalpha() and action.lower() == 'no':
            print()
            return f"You refused to {msg} the note."
        else:
            print('=' * 50)
            print("Incorrect input! Please, enter 'yes' or 'no'.")
            print('=' * 50)


def check_day():
    while True:
        try:
            number = int(input(f"Enter the date of month: "))
            if 1 <= number <= 31:
                return number
            else:
                print('=' * 50)
                print("Incorrect input! The number must be in the range from 1 to 31!")
                print('=' * 50)
        except ValueError:
            print('=' * 50)
            print("Incorrect input! It's not a number!")
            print('=' * 50)
