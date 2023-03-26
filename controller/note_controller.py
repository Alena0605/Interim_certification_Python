from models.note_operations import NoteOperations
from models.note import Note
import exceptions as ex

from tabulate import tabulate


class NoteController:
    __n_o = NoteOperations()

    def create_note(self):
        return self.__n_o.add_note()

    def change_note(self):
        return self.__n_o.update_note()

    def delete_note(self):
        return self.__n_o.remove_note()

    def read_all(self):
        result = self.__n_o.read_all_notes()

        if type(result) is list:
            return f'{tabulate(result, headers=["DATA", "ID", "TITLE", "DESCRIPTION"])}\n'

        return result

    def search_note_by_id(self):
        result = self.__n_o.read_all_notes()

        if type(result) is list:
            data = ex.check_note(result)
            searching_note = Note(data[1], data[2], data[3], data[0])
            print()
            return searching_note

        return result

    def search_note_by_title(self):
        result = self.__n_o.read_all_notes()

        if type(result) is list:
            title = input("Enter the title of note you want to find: ")

            if not title:
                title = 'NO TITLE'

            searching_notes_by_title = []
            count = 0

            for note in result:
                if title.upper() == note[2]:
                    searching_notes_by_title.append(note)
                    count += 1

            if len(searching_notes_by_title) == 0:
                return "Note not found!\n"

            return f"Found {count} notes:\n\n" \
                   f"{tabulate(searching_notes_by_title, headers=['DATA', 'ID', 'TITLE', 'DESCRIPTION'])}\n"

        else:
            return result

    def search_note_by_month(self, number: int):
        result = self.__n_o.read_all_notes()

        if type(result) is list:
            searching_notes_by_date = []
            count = 0

            for note in result:
                month = note[0].split()[0].split('-')[1]
                if number == int(month):
                    searching_notes_by_date.append(note)
                    count += 1

            if len(searching_notes_by_date) == 0:
                return "Note not found!\n"

            return f"Found {count} notes:\n\n" \
                   f"{tabulate(searching_notes_by_date, headers=['DATA', 'ID', 'TITLE', 'DESCRIPTION'])}\n"

        else:
            print()
            return result
