# class Person:

#     population  = 0
#     def __init__(self,name):
#         self.name = name
#         Person.population +=1
#     def sayHi(self):
#         print("Hi {}".format(self.name))
    
#     @classmethod
#     def popcount(Person):
#         print(Person.population)

# p = Person("Ken");
# p.sayHi()
# p.popcount()
# print(p)


# k = Person("osei");
# k.sayHi()
# k.popcount()
# print(k)

#INHERITANCE

# class Rectangle:

#     def __init__(self,length=0, width=0):
#         self.length = length
#         self.width = width

#     def calculateaarea(self):
#         return self.length * self.width
    
#     def calculateperimeter(self):
#         return ((self.length*2) + (self.width*2))
    

# class Square(Rectangle):
#     def __init__(self, length=0):
#         # self.length =length
#         # self.width = length
#         super().__init__(length,length)


# sq = Square(4)

# print("{}".format(sq.calculateaarea()))



#ENCAPSULATION

# class Person:
#     def __init__(self,name, age):
#         self._age= age
#         self._name= name

#     @property
#     def get_name(self):
#         return self._name
    
#     @get_name.setter
#     def set_name(self,value):
#         self._name = value

#     @property
#     def get_age(self):
#         return self._age
    
#     @get_age.setter
#     def set_age(self,value):
#         self._age =value

# p= Person("ken", 21)

# print(p.get_age)


#POLYMORPHISM

# class Shape:

#     def Area(self):
#         return 0;


# class Circle(Shape):
#     def __init__(self, radius="0"):
#         self.radius =radius

#     def Area(self):
#         return 0.5 * 3.142 * self.radius

# class Triangle(Shape):
#     def __init__(self, base=0, height=0):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height



# COMPOSITION


# class Engine:
#     def __init__(self,horsepower):
#         self._horsepower = horsepower

#     @property
#     def get_horsepower(self):
#         return self._horsepower
    
#     @get_horsepower.setter
#     def set_horsepower(self,value):
#         self._horsepower = value


# class Wheels:
#     def __init__(self, size):
#         self._size = size

#     @property
#     def get_size(self):
#         return self._size
    
#     @get_size.setter
#     def set_size(self, value):
#         self._size = value

# class Car:
#     def __init__(self,engine, wheels):
#         self._engine= engine
#         self._wheels = wheels


#ABSTRACTION


# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def make_sound(self, sound):
#         print("{} is {}ing".format(self.name,sound))

# class Dog(Animal):
#     __sound = "bark"
#     def __init__(self,name):
#         super().__init__(name)

#     def make_sound(self):
#         super().make_sound(Dog.__sound)


# class Cat(Animal):
#     __sound = "meow"
#     def __init__(self,name):
#         super().__init__(name)

#     def make_sound(self):
#         super().make_sound(Cat.__sound)


# ca = Cat("Pus")

# ca.make_sound()

# do = Dog("Peace")

# do.make_sound()

#METHOD OVERLOADING

# class Calculator:
#     def add(self,*lis):
#         sum =0
#         for i in lis:
#             sum+=i
#         return sum

#     def multiply(self,*lis):
#         mul = 1

#         for i in lis:
#             mul *= i
        
#         return mul
    

# cal = Calculator();

# print(cal.multiply(1,2,3,6,2))



#CLASS ATTRIBUTES


# class Counter:
#     __count=0
#     def __init__(self):
#         Counter.__count+=1

# p = Counter()


# class Counter:
#     __counter= 0

#     def __init__(self):
#         self.increase()

#     @classmethod
#     def increase(cls):
#         cls.__counter+=1


# c = Counter()

#STATIC METHODS

# class Math:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
# result = Math.add(3, 5)
# print("Result of addition:", result)

class Car:
    def __init__(self,make, year, model):
        self._make = make
        self._model = model
        self._year = year

    def display_info(self):
        print("Make:{}\nModel:{}\nYear:{}".format(self._make,self._model,self._year))

mas = Car("Toyota", 2007,"Fielder")

mas.display_info()