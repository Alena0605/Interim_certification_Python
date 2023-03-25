import csv
from os import path


class FileOperations:
    __filename_csv = "notes.csv"

    def read_csv(self):
        if not path.exists(self.__filename_csv):
            return "ERROR! File does not exist! You have not created any notes yet."

        __rows = []

        with open(self.__filename_csv, encoding="utf-8") as f_reader:
            if path.getsize(self.__filename_csv) == 0:
                return "File is empty!"

            file_reader = csv.reader(f_reader, delimiter=";")

            for row in file_reader:
                __rows.append(row)

        return __rows

    def save_csv(self, note):
        with open(self.__filename_csv, 'a', encoding='utf-8') as f:
            f_writer = csv.writer(f, delimiter=';', lineterminator="\r")
            f_writer.writerow([note.get_date(), note.get_id(), note.get_title(), note.get_text()])

    def rewriter_csv(self, notes_list):
        with open(self.__filename_csv, 'w', encoding='utf-8') as f:
            f_writer = csv.writer(f, delimiter=';', lineterminator="\r")
            for note in notes_list:
                f_writer.writerow([note[0], note[1], note[2], note[3]])
