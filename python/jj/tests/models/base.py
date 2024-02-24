import json
from rectangle import Rectangle
from square import Square
import csv
import turtle

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if(id):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects+ 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        with open(f"{cls.__name__}.json","w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(2,3)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new
    
    @classmethod
    def load_from_file(cls):
        # with open(f"{cls.__name__}.json","r") as f:
        #     newli = cls.from_json_string(f.read())

        #     for dic in newli:
        #         cls.create(dic)

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__

        with open(f"{filename}.csv", "w") as f:
            if list_objs:
                header = list(list_objs[0].keys())
                f.write(",".join(header) + "\n")

                for obj in list_objs:
                    values = [str(obj[key]) for key in header]
                    f.write(",".join(values) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        with open(filename, "r") as f:
            headli = f.readline().strip().split(",")

            mainli = []
            for line in f:
                newdict = {}
                newline = line.strip().split(",")

                for i in range(len(headli)):
                    newdict[headli[i]] = int(newline[i])  # Convert to int

                mainli.append(newdict)

        return mainli

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.color("red")
        for rect in list_rectangles:
            rect = Rectangle(**rect)
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)

        for square in list_squares:
            square = Square(**square)
            turtle.color("blue")
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.forward(square.width)
            turtle.right(90)
            turtle.forward(square.height)
            turtle.right(90)
            turtle.forward(square.width)
            turtle.right(90)
            turtle.forward(square.height)

        turtle.done()