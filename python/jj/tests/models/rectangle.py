from base import Base

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

    def __str__(self):
        return f"[Rectangle] {self.id} {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        if(len(args) >=1):
            self.id = args[0]
        if(len(args) >=2):
            self.__width = args[1]
        if(len(args)>=3):
            self.__height = args[2]
        if(len(args)>=4):
            self.__x = args[3]
        if(len(args)>=5): 
            self.__y = args[4]



r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)