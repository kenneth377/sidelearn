# class Person:

#     __population =0

#     def __init__(self,name,age):
#         self._name = name
#         self._age = age

#     # @classmethod
#     # def popget(cls):
#     #     return cls.__population
    
#     @property
#     def get_name(self):
#         return self._name
    
#     @get_name.setter
#     def set_name(self, value):
#         self._name = value


# person = Person("kwame", 44)
# person.set_name ="baba"
# person.__population =2
# Person.__population =555
# # print(person.popget())

# print(person.__population)
# print(Person.__dict__["__population"])


#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0,):
        if width < 0  or height<0:
            raise ValueError("Width and Height must be greater than zero")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances+=1


    @property
    def height(self):
        return self.__height
    
    @property
    def width(self):
        return self.__width
    
    
    @height.setter
    def height(self,value):
        if isinstance(value,int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("heigth must be >= 0")
        else:
            raise TypeError("heigth must be an integer")

    @width.setter
    def width(self,value):
        if isinstance(value,int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        
    def area(self):
        """Return the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2*self.__width)+(2*self.__height))
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        
        return "\n".join([str(self.print_symbol)*self.__width]*self.__height)
    
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances-=1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1,Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)