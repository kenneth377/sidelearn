import json
import csv

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

        with open(f"{filename}.csv","w") as f:
            header = list(list_objs[0].keys() if list_objs else [])
            newstr = ",".join([attr for attr in header])
            f.write(newstr+"\n")
            newli = ""

            for obj in list_objs:
                newstr = ",".join(str(obj[attr]) for attr in header)
                f.write(newstr+ "\n")
    
    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__

        with open(f"{filename}.csv", "r") as f:

            newli = []

            id = list(f.readline())