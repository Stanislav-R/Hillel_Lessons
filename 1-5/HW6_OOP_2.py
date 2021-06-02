# OOP_2: Class Point&Circle
import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, p):
        if (abs(p.x - self.x) ** 2 + abs(p.y - self.y) ** 2) <= self.radius ** 2:
            return True
        else:
            return False


p = Point(100, 100)
c = Circle(100, 100, 1)
print(c.contains(p))
