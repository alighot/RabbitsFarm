import json

from Carrot import Carrot
from Field import Field
from Rabbit import Rabbit
from view import View
import JsonHandler
from time import sleep
import os
import Exceptions


def deserialize_objects(obj):
    if obj['class'] == "Field":
        field = Field(obj['width'],
                      obj['height'],
                      obj['date'],
                      obj['field_map'],
                      obj['rabbits'],
                      obj['carrots'],
                      obj['empty_rooms'])
        return field
    elif obj['class'] == "Rabbit":
        rabbit = Rabbit(obj['born_date'],
                        obj['location'],
                        obj['gender'])
        rabbit.health = obj['health']
        return rabbit
    elif obj['class'] == "Carrot":
        carrot = Carrot(obj['born_date'],
                        obj['location'])
        return carrot
    else:
        print("Cant find class")
        raise ValueError


class FieldController(object):
    def __init__(self):
        self.view = View()
        self.field = self.create_field_if_not_exist()

    def create_field_if_not_exist(self):
        if not os.path.exists("field.json"):
            try:
                print("Please insert ")
                print("width:", end=" ")
                width = int(input())
                print("height:", end=" ")
                height = int(input())
                field = Field(width, height)
            except:
                print("values are not acceptable. using default values")
                field = Field()
            text = input("prompt")
            return field
        else:
            field = FieldController.load_from_json("field.json")
            self.view.show_preview(field.date, field.number_of_rabbits, field.number_of_carrots)
            print("Are you want to load this field?")
            input_bool = input()
            if input_bool == "yes":
                self.view.clear()
                return field
            elif input_bool == "no":
                try:
                    print("Please insert ")
                    print("width:", end=" ")
                    width = int(input())
                    print("height:", end=" ")
                    height = int(input())
                    field = Field(width, height)
                except ValueError:
                    print("values are not acceptable. using default values")
                    field = Field()
                return field
            else:
                print("Your answer is not acceptable! Your answer must be 'yes' or 'no'. Loading from file")
                return field

    @staticmethod
    def load_from_json(file_address):
        with open(file_address) as j_file:
            j_data = j_file.read()
            field = json.loads(j_data, object_hook=deserialize_objects)
        return field

    @staticmethod
    def save_to_json_file(obj, file_address):
        with open(file_address, 'w') as j_file:
            j_file.truncate(0)
            json.dump(obj, j_file, indent=4, default=JsonHandler.serialize_objects)

    def daily_show(self):
        last_rabbit_location = ""
        last_carrot_location = ""
        exception = []
        try:
            last_rabbit_location = self.field.last_borned_rabbit.location
        except Exceptions.NoMoreRabbit:
            last_rabbit_location = " "
            exception += ['No More Rabbit']
        try:
            last_carrot_location = self.field.last_created_carrot.location
        except Exceptions.NoMoreCarrot:
            last_carrot_location = " "
            exception += ['No More Carrot']
        except Exceptions.NoMoreRooms:
            # TODO handel exception
            exception += ['No More Room']

        self.view.clear()
        self.view.show(self.field.field_map,
                       self.field.date,
                       last_rabbit_location,
                       last_carrot_location,
                       self.field.number_of_rabbits,
                       self.field.number_of_carrots,
                       exception=exception)

    def start(self):
        if self.field.date == 1:
            for _ in range(2):
                self.field.add_rabbit(gender="Male")
                self.field.add_rabbit(gender="Female")
                self.field.add_carrot()
                self.field.add_carrot()
        self.daily_show()
        self.save_to_json_file(self.field, "field.json")
        self.life_loop()

    def life_loop(self):
        while True:
            self.field.date += 1
            self.field.add_carrot()
            self.field.move_rabbits()
            self.daily_show()
            self.save_to_json_file(self.field, "field.json")
            sleep(3)


# if __name__ == '__main__':
f_c = FieldController()
f_c.start()
