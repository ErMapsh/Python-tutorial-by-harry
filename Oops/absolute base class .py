from abc import ABCMeta, abstractclassmethod, ABC
#abstract class = in that class metaclass has defined that being a abstract class, class having some abstract class methods 
#if u inherited from that class u should do abstract method to another class. means child should have some parent skill like that
class Shape(metaclass = ABCMeta):
    @abstractclassmethod
    def print_area(cls):
        return 0

class Rectangle(Shape):
    _type = "Rectangle"
    side = 4

    def __init__(self):
        self.length = 4
        self.breath = 6

    def print_area(self):
        return self.length * self.breath


Rect = Rectangle()
print(Rect.print_area())

