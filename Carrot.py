import uuid


class Carrot(object):
    def __init__(self, born_date, location):
        self.__id = uuid.uuid1().int
        self.__born_date = born_date
        self.location = location

    @property
    def id(self):
        """getter of id property"""
        return self.__id

    @property
    def born_date(self):
        """getter of born_date property"""
        return self.__born_date

    def __str__(self):
        return "C"

    def __eq__(self, other):
        if isinstance(other, Carrot):
            if self.id == other.id:
                return True
            else:
                return False
