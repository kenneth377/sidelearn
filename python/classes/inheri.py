# """dir(obj) - is used to return the available attributes and methods of an object"""


# # class Person(object):
# #     def __init__(self,name):
# #         self.name =name

# # person1 = Person("Kenneth")

# # def lookup(obj):
# #     return dir(obj)

# # print(lookup(person1))


# class MyList(list):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
    
#     def print_sorted(self):
#         print(sorted(self))

# def is_same_class(obj, a_class):
#     return isinstance(obj, a_class)

# def is_kind_of_class(obj, a_class):
#     return isinstance(obj, a_class)

# my_list = MyList()
# my_list.append(1)
# my_list.append(4)
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)

# l1 = [1, 2, 3]
# dig = 33

# print(is_same_class(l1,MyList))
# print(is_kind_of_class(l1,MyList))
# # print(is_same_class(my_list,Mylist))
# # print(is_same_class(dig,Mylist))


# class BaseGeometry:
#     pass

#     def area(self):
#         raise Exception("area() is not implemented")

#     def integer_validator(self, name, value):
#         if not isinstance(value,int):
#             raise TypeError(f"{name} must be an integer")
#         if value <= 0:
#             raise ValueError(f"{name} must be greater than 0")

# class Rectangle(BaseGeometry):
#     def __init__(self,width,height):
#         self.integer_validator("HEIGHT", height)
#         self.integer_validator("width", width)
        
#         self.__width = width
#         self.__height = height

#     def area(self):
#         return self.__width * self.__height
    
#     def __str__(self):
#         return f"[Rectangle] {self.__width}/{self.__height}"
    
# class Square(Rectangle):
#     def __init__(self, size):
#         self.integer_validator("size", size)
#         super().__init__(size, size)




# class MyInt(int):
#     def __eq__(self, other):
#         return super().__ne__(other)

#     def __ne__(self, other):
#         return super().__eq__(other)

#     def __add__(self,value):
#         return 100
    

# print(2+2)
# print( 2==2)
# print(2!=2)

# mint1 = MyInt(2)
# mint2 = MyInt(2)

# print(mint2+mint1);
# print( mint2== mint1)
# print(mint2!= mint1)


# def add_attribute(obj, attr, value):
#     # Set the attribute
#     setattr(obj, attr, value)
#     # Check if the attribute has been added successfully
#     if getattr(obj, attr) != value:
#         # If not, raise a TypeError
#         raise TypeError("can't add new attribute")