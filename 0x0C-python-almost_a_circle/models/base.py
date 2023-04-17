#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv
import turtle



class Base:
    """A representation of the base of our OOP hierarchy."""
    __nb_objects = 0

    """Constructor"""


    def __init__(self, id=None):        
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries) 

    @staticmethod
    def from_json_string(json_string):
        """Unjsonifies a dictionary."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries

        Returns:
            list: list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Loads instance from dictionary."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        instances = []
        for dictionary in list_dicts:
            instance = cls.create(**dictionary)
            instances.append(instance)
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object."""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Loads object."""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

        @staticmethod
        def draw(list_rectangles, list_squares):
            screen = turtle.Screen()
            screen.setup(width=800, height=600)
            screen.title("Rectangles and Squares")

            pen = turtle.Turtle()
            pen.speed(0)

            for rect in list_rectangles:
                pen.penup()
                pen.goto(rect.x, rect.y)
                pen.pendown()
                pen.color("blue")
              for _ in range(2):
                    pen.forward(rect.width)
                    pen.left(90)
                  pen.forward(rect.height)
                   pen.left(90)

            for square in list_squares:
                pen.penup()
                pen.goto(square.x, square.y)
                pen.pendown()
                pen.color("red")
                for _ in range(4):
                    pen.forward(square.size)
                    pen.left(90)

            turtle.done()

