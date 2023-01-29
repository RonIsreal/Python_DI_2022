'''Daily Challenge - Circle

Instructions :
The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area
Print the circle and get something nice
Be able to add two circles together
Be able to compare two circles to see which is bigger
Be able to compare two circles and see if there are equal
Be able to put them in a list and sort them'''
import math as m

class Circle:

    def __init__(self, radius=5):
        self.radius = radius
        self.diameter = self.diameter()
        self.area = self.area()
        self.circles_sorted = []

    def diameter(self):
        return float(self.radius * 2)

    def area(self):
        return float("%2f" % (m.pi * pow(self.radius,2)))

    def add_circles(self, other):
        return self.radius + other.radius

    def compare_circles(self, other):
        if self.radius > other.radius:
            return f"Your circle is bigger than the other. Your radius: {self.radius} > Other radius: {other.radius}."
        elif self.radius == other.radius:
            return f"Both circles are the same size. Your radius: {self.radius} = Other radius: {other.radius}."
        else:
            return f"The other circle is bigger than yours. Your radius: {self.radius} < Other radius: {other.radius}"

    def sort_circles(self, other):
        self.circles_sorted.append(self.circles_sorted.sort(key=lambda x: x.radius))
        return self.circles_sorted




    def __repr__(self):
        return f"Your circle's info:\nRADIUS: {self.radius}\nDIAMETER: {self.diameter}\nAREA: {self.area}"

my_circle = Circle(4)
my_circle2 = Circle()
print(my_circle.area)
print(my_circle.__repr__())
print(my_circle.add_circles(my_circle2))
print(my_circle.compare_circles(my_circle2))
print(my_circle.sort_circles(my_circle2))


