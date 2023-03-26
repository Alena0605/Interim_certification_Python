from models.file_operations import FileOperations
from models.note import Note
import exceptions as ex


class NoteOperations:
    __fo = FileOperations()

    def add_note(self):
        answer = self.__fo.read_csv()

        if type(answer) is list:
            max_index = len(answer)
            new_index = max_index + 1
        else:
            new_index = 1

        data = ex.input_data()

        if not data[1]:
            print()
            return "You interrupted the creating of note.\n"

        note = Note(new_index, data[0], data[1], data[2])
        self.__fo.save_csv(note)

        return "Note created!\n"

    def update_note(self):
        answer = self.__fo.read_csv()

        if type(answer) is list:
            note = ex.check_note(answer)
            note_for_change = Note(note[1], note[2], note[3], note[0])
            print()
            print(note_for_change)
            print()

            index = answer.index(note)
            accep = ex.check_chosen_note(answer, index, 'change')

            if type(accep) is list:
                while True:
                    print()
                    print("=" * 50)
                    print("Choose parameter you want to change:")
                    print("=" * 50)
                    print("\t1. Title\n"
                          "\t2. Description\n"
                          "\t0. Cancel\n")

                    param = ex.check_input("Enter the operation number")

                    if param == 1:
                        title = ex.check_title()
                        note_for_change.set_date()
                        note_for_change.set_title(title)
                    elif param == 2:
                        text = ex.check_text("Add new description")
                        if not text:
                            print()
                            return "You interrupted the changing of note.\n"
                        note_for_change.set_date()
                        note_for_change.set_text(text)
                    elif param == 0:
                        print()
                        return "You interrupted the changing of note.\n"
                    else:
                        print("=" * 50)
                        print("Incorrect input! Please, choose something from the list!")
                        print("=" * 50)
                        continue

                    accep.insert(index, [note_for_change.get_date(), note_for_change.get_id(),
                                         note_for_change.get_title(), note_for_change.get_text()])
                    self.__fo.rewriter_csv(accep)

                    return "Note changed.\n"
            else:
                return accep

        else:
            return answer

    def remove_note(self):
        answer = self.__fo.read_csv()

        if type(answer) is list:
            note = ex.check_note(answer)
            note_for_change = Note(note[1], note[2], note[3], note[0])
            print()
            print(note_for_change)
            print()

            index = answer.index(note)
            accep = ex.check_chosen_note(answer, index, 'delete')

            if type(accep) is list:
                self.__fo.rewriter_csv(accep)
                return "Note deleted.\n"
            else:
                return accep

        else:
            return answer

    def read_all_notes(self):
        answer = self.__fo.read_csv()
        return answer
