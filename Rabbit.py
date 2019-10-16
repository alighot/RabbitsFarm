import logging
import random
import uuid
import Exceptions


class Rabbit(object):
    def __init__(self, born_date, location, gender=None):
        if not gender:
            gender = "Male" if random.randrange(2) == 1 else "Female"
        self.__id = uuid.uuid1().int
        self.__born_date = born_date
        self.location = location
        self.__gender = gender
        logging.debug(gender)
        self.__health = 200
        self.memory = {'empty_rooms': [],
                       'rabbits': [],
                       'carrots': []
                       }

    @property
    def id(self):
        return self.__id

    @property
    def born_date(self):
        """getter of born_date property"""
        return self.__born_date

    @property
    def gender(self):
        """getter of gender property"""
        return self.__gender

    @property
    def health(self):
        """getter of health property"""
        return self.__health

    @health.setter
    def health(self, new_value):
        """setter of health property"""
        if 0 < new_value <= 200:
            self.__health = new_value
        elif new_value > 200:
            self.__health = 200
        elif new_value <= 0:
            raise Exceptions.RabbitMustBeDied

    def __str__(self):
        return "R"

    def __eq__(self, other):
        if isinstance(other, Rabbit):
            if self.id == other.id:
                return True
            else:
                return False
