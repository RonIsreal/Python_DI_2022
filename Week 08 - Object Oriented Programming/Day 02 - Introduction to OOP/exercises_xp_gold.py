'''Exercise 1 : Geometry
Instructions
Write a class called Circle that receives a radius as an argument (default is 1.0).
Write two instance methods to compute perimeter and area.
Write a method that prints the geometrical definition of a circle.'''

class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius**2
        print(area)

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        print(perimeter)

    def circle_definition(self):
        print("A circle is a round-shaped figure that has no corners or edges.")

my_circle = Circle()
my_circle.calculate_area()
my_circle.calculate_perimeter()
my_circle.circle_definition()

'''Exercise 2 : Custom List Class
Instructions
Create a class called MyList, the class should receive a list of letters.
Add a method that returns the reversed list.
Add a method that returns the sorted list.
Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).'''

import random

random.seed()

class MyList:
    def __init__(self, letters):
        self.letters = list(letters)

    def reverse_list(self):
        reversed_list = list(reversed(self.letters))
        return reversed_list

    def sorted_list(self):
        list_sorted = sorted(self.letters)
        return list_sorted

    def second_list(self):
        list_two = []
        len(list_two) == len(self.letters)
        list_two.append([random.randint(0,999) for _ in range(len(self.letters))])
        return list_two

my_list = MyList('abzefd')
print(my_list.letters)
print(my_list.reverse_list())
print(my_list.sorted_list())
print(my_list.second_list())





