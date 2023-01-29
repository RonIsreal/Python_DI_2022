'''Analyse the code below. What will be the outputs ?

Explain the goal of the methods

'''

class Circle:
    color = "red"

    def __init__(self, diameter): #method to initialize the class. Needs a parameter value
        self.diameter = diameter

    def grow(self, factor=2): #method to calculate the new diameter of the circle class. It can accept a factor to multiply or by default multiply by 2
        self.diameter = self.diameter * factor

    def get_color(self): #return the current color of the class Circle
       return Circle.color

circle1 = Circle(2)
print(circle1.color) #red
print(Circle.color) #red
print(circle1.get_color()) #red
circle1.grow(3) #nothing, just multiplied
print(circle1.diameter) #6

'''Analyze the code below. What will be the ouput ?'''

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val()) #Value of object : 10
print(MyClass.get_count()) #1

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val()) #Value of object : 20
print(MyClass.get_count()) #2 because the init is counting the MyClass object everytime it is called

object_3 = MyClass(30)
print("\nValue of object : %s" % object_3.get_val()) #Value of object : 30
print(MyClass.get_count()) #3

'''Analyze the code below. What will be the ouput ?'''

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val) #5
print(b.val) #10
print(c.val) #15
print(a.filterint(100)) #100

'''Analyse the code below before executing it. What will be the output ?'''

class PrintList(object):

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return self.mylist


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__()) #['a','b','c']