from datetime import datetime


class Human:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date
