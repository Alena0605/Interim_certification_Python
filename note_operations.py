from file_operations import FileOperations
import exceptions as ex
from note import Note


class NoteOperations:
    __fo = FileOperations()
    __answer = __fo.read_csv()

    def create_note(self):
        if type(self.__answer) is list:
            max_index = len(self.__answer)
            new_index = max_index + 1
        else:
            new_index = 1

        data = ex.input_data()

        if not data[1]:
            print()
            return "You interrupted the creating of note."

        note = Note(new_index, data[0], data[1], data[2])
        self.__fo.save_csv(note)

        return "The note is created!"

    def change_note(self):
        note = ex.check_note(self.__answer)
        note_for_change = Note(note[1], note[2], note[3], note[0])
        print(note_for_change)
        index = self.__answer.index(note)
        self.__answer.pop(index)

        while True:
            print("Choose parameter you want to change:\n"
                  "\t1. Title\n"
                  "\t2. Description\n")

            param = ex.check_input("Enter the number from the list: ")

            if param == 1:
                title = ex.check_title()
                note_for_change.set_date()
                note_for_change.set_title(title)
            elif param == 2:
                text = ex.check_text("Add new description")
                if not text:
                    print()
                    return "You interrupted the changing of note."
                note_for_change.set_date()
                note_for_change.set_text(text)
            else:
                print("Incorrect input! Please, choose something from the list!")

            self.__answer.insert(index, [note_for_change.get_date(), note_for_change.get_id(),
                                         note_for_change.get_title(), note_for_change.get_text()])
            self.__fo.rewriter_csv(self.__answer)
            print(note_for_change)

            return "The data overwritten."
