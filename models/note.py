from datetime import datetime as dt


class Note:
    def __init__(self, id: int, title: str, text: str, date: str):
        self.__id = id
        self.__title = title
        self.__text = text
        self.__date = date

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_text(self):
        return self.__text

    def set_text(self, text: str):
        self.__text = text

    def get_date(self):
        return self.__date

    def set_date(self):
        self.__date = dt.now().strftime('%Y-%m-%d %A %H:%M')

    def __str__(self):
        return f"{self.__id} {self.__title}\n{self.__date}\n{self.__text}\n"
