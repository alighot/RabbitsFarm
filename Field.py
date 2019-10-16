from Carrot import Carrot
from Rabbit import Rabbit
import Exceptions
import random
from time import sleep


class Field(object):
    def __init__(self, width=14, height=14, date=1, field_map=[], rabbits=[], carrots=[], empty_rooms=[]):
        self.__width = width
        self.__height = height
        self.date = date
        self.__field_map = field_map
        self.__rabbits = rabbits
        self.__carrots = carrots
        self.__empty_rooms = empty_rooms
        for y in range(height):
            self.__field_map.append([])
            is_horizonatl = y == 0 or y == height - 1
            for x in range(width):
                is_vertical = x == 0 or x == width - 1
                if is_horizonatl and is_vertical:
                    self.__field_map[y].append(".")
                elif is_vertical:
                    self.__field_map[y].append("|")
                elif is_horizonatl:
                    self.__field_map[y].append("_")
                else:
                    self.__field_map[y].append(" ")
                    self.__empty_rooms.append([y, x])

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def field_map(self):
        return self.__field_map

    @property
    def number_of_rabbits(self):
        return len(self.__rabbits)

    @property
    def number_of_carrots(self):
        return len(self.__carrots)

    @property
    def rabbits(self):
        return self.__rabbits

    @property
    def carrots(self):
        return self.__carrots

    @property
    def empty_rooms(self):
        return self.__empty_rooms

    @property
    def last_borned_rabbit(self):
        try:
            rabbit = sorted(self.rabbits, key=lambda x: x.born_date).pop()
            return rabbit
        except IndexError:
            raise Exceptions.NoMoreRabbit

    @property
    def last_created_carrot(self):
        try:
            carrot = sorted(self.carrots, key=lambda x: x.born_date).pop()
            return carrot
        except IndexError:
            raise Exceptions.NoMoreCarrot

    def __random_empty_point(self):
        try:
            return self.__empty_rooms[random.randrange(len(self.__empty_rooms))]
        except ValueError:
            raise Exceptions.NoMoreRooms

    def add_carrot(self):
        try:
            location = self.__random_empty_point()
        except Exceptions.NoMoreRooms:
            raise Exceptions.NoMoreRooms
        new_carrot = Carrot(self.date, location)
        self.__field_map[location[0]][location[1]] = new_carrot
        self.__carrots.append(new_carrot)
        self.__empty_rooms.remove(location)

    def add_rabbit(self, gender=""):
        location = self.__random_empty_point()
        new_rabbit = Rabbit(self.date, location) if gender == "" else Rabbit(self.date, location, gender)
        self.__field_map[location[0]][location[1]] = new_rabbit
        self.__rabbits.append(new_rabbit)
        self.__empty_rooms.remove(location)

    def __remove_rabbit(self, rabbit):
        self.__field_map[rabbit.location[0]][rabbit.location[1]] = " "
        self.__empty_rooms.append(rabbit.location)
        try:
            self.__rabbits.remove(rabbit)
        except ValueError:
            pass

    def __born_rabbit(self, parents):
        self.add_rabbit()
        for rabbit in parents:
            try:
                rabbit.health -= 50
            except Exceptions.RabbitMustBeDied:
                self.__remove_rabbit(rabbit)

    def __move_rabbit(self, rabbit, location):
        self.__field_map[rabbit.location[0]][rabbit.location[1]] = " "
        self.__empty_rooms.append(rabbit.location)
        self.__field_map[location[0]][location[1]] = rabbit
        rabbit.location = location
        try:
            rabbit.health -= 10
        except Exceptions.RabbitMustBeDied:
            self.__remove_rabbit(rabbit)

    def move_rabbits(self):
        for rabbit in self.rabbits:
            for i in range(20):
                y_offset = random.randrange(-1, 2)
                x_offset = random.randrange(-1, 2)
                new_location = [rabbit.location[0] + y_offset, rabbit.location[1] + x_offset]
                if self.__field_map[new_location[0]][new_location[1]].__str__() == " ":
                    self.__move_rabbit(rabbit, new_location)
                    self.__empty_rooms.remove(new_location)
                    break
                elif self.__field_map[new_location[0]][new_location[1]].__str__() == "C":
                    self.__carrots.remove(self.__field_map[new_location[0]][new_location[1]])
                    self.__move_rabbit(rabbit, new_location)
                    rabbit.health += 20
                    break
            for y in range(rabbit.location[0] - 1, rabbit.location[0] + 2):
                for x in range(rabbit.location[1] - 1, rabbit.location[1] + 2):
                    if isinstance(self.field_map[y][x], Rabbit):
                        if rabbit.gender != self.field_map[y][x].gender:
                            self.__born_rabbit([rabbit, self.field_map[y][x]])
