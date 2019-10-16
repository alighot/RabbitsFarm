from Carrot import Carrot
from Rabbit import Rabbit
from Field import Field


def serialize_objects(obj):
    if isinstance(obj, Field):
        return {
            'class': Field.__name__,
            'width': obj.width,
            'height': obj.height,
            'field_map': obj.field_map,
            'date': obj.date,
            'rabbits': obj.rabbits,
            'carrots': obj.carrots,
            'empty_rooms': obj.empty_rooms
        }
    elif isinstance(obj, Rabbit):
        return {
            'class': Rabbit.__name__,
            'location': obj.location,
            'born_date': obj.born_date,
            'gender': obj.gender,
            'health': obj.health
        }
    elif isinstance(obj, Carrot):
        return {
            'class': Carrot.__name__,
            'location': obj.location,
            'born_date': obj.born_date
        }
    raise TypeError(str(obj) + ' is not JSON serializable')


def deserialize_objects(obj):
    if obj['class'] == "Filed":
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
