from base import Base
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.__size =size
        super().__init__(width=self.__size, height=self.__size,x=x,y=y,id =id)
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value

    
    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value    

    def __str__(self):
        return f"[Square] {self.id} {self.x}/{self.y} - {self.size}"


    def to_dictionary(self):
        return {
            "id": self.id,
            "size":self.__size,
            "x": self.x,
            "y": self.y
        }
    

if __name__ == "__main__":
    from rectangle import Rectangle