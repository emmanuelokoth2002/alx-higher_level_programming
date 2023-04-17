#!/usr/bin/python3
import json
import csv
import turtle

"""Class defination"""


class Base:
     """A representation of the base of our OOP hierarchy."""


    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""


        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """sonifies a dictionary so it's quite rightly and longer."""


        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves jsonified object to file."""


        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Unjsonifies a dictionary."""


        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Loads instance from dictionary"""


        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads string from file and unjsonifies."""


        filename = cls.__name__ + ".json"
        obj_list = []
        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                obj_list_dicts = cls.from_json_string(my_file.read())
                for obj_dict in obj_list_dicts:
                    obj_list.append(cls.create(**obj_dict))
        except FileNotFoundError:
            pass
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object to csv file."""


        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as my_file:
            if list_objs is not None:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(my_file, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads object to csv file."""


        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode="r", newline="") as my_file:
                reader = csv.DictReader(my_file)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    obj_list.append(cls.create(**row))
        except FileNotFoundError:
            pass
        return obj_list

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""


        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""


        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a function"""


        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""


        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as f:
                json_str = f.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for r in list_objs:
                    writer.writerow([r.id, r.width, r.height, r.x, r.y])
            elif cls.__name__ == "Square":
                for s in list_objs:
                    writer.writerow([s.id, s.size, s.x, s.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    return [cls(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])) for row in reader]
                elif cls.__name__ == "Square":
                    return [cls(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])) for row in reader]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        t = turtle.Turtle()
        t.speed(1)
        t.penup()
        for rect in list_rectangles:
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()
        for square in list_squares:
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.penup()
        window.exitonclick()        
