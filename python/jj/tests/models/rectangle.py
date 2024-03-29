


class Rectangle(Base):


    def __init__(self, width, height, x=0, y=0, id=None):
        self.__y = y
        self.__x = x
        self.__height = height
        self.__width = width
        
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @width.setter
    def width(self,value):
        if( type(value) != int):
            raise TypeError(f"Width must be an integer")
        elif( value <0):
            raise ValueError("Width must be >= 0")
        self.__width = value

    @height.setter
    def height(self,value):
        if( type(value) != int):
            raise TypeError(f"Height must be an integer")
        elif( value <=0):
            raise ValueError("Height must be >= 0")
        self.__height = value

    @x.setter
    def x(self,value):
        if( type(value) != int):
            raise TypeError(f"X must be an integer")
        elif( value <0):
            raise ValueError("X must be >= 0")
        self.__x = value
    
    @y.setter
    def y(self,value):
        if( type(value) != int):
            raise TypeError(f"Y must be an integer")
        elif( value <0):
            raise ValueError("Y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width
    
    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                    print(" ", end = "")
            for i in range(self.__width):
                print("#", end = "")

            print()

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def __str__(self):
        return f"[Rectangle] {self.id} {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
 

if __name__ == "__main__":


    r1 = Rectangle(1,1,4,4)
    r2 = Rectangle(2,2, 8,8)

    Rectangle.save_to_file_csv([r1.to_dictionary(),r2.to_dictionary()])

    print(Rectangle.load_from_file_csv())

    s1 = Square(1,1,4,4)
    s2 = Square(2,2, 8,8)

    Rectangle.save_to_file_csv([s1.to_dictionary(),s2.to_dictionary()])

    Base.draw(Rectangle.load_from_file_csv(), Square.load_from_file_csv())
