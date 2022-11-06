'''Exercise 1:

Analyse the code below before executing it. What will be the outputs ?

class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)
# >> What will be the output ?


class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)
# >> What will be the output'''

class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color) #blue

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2) #1 - specified diameter * 2 - standard factor value * 2

nc = NewCircle(1)
print(nc.diameter) #1

nc.grow() #Function to calculate the new diameter according to user input

print(nc.diameter) #4

'''Exercise 2:

What is the difference between these 2 pieces of code ?

class A(B):
    def __init__(self, *args, **kwargs)
        B.__init__(self, *args, **kwargs)
        pass


class A(B):
    def __init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        pass
'''

#Even though one has the super() function and the other is calling directly the __init__, there is technically no difference between these codes.

'''Exercise 3: 

Try to recreate the class explained below:

We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, 
which simply raises an Error that a blocked door cannot be opened or closed.'''

class Door:
    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        print("The door has been opened.")

    def close_door(self):
        print("The door has been closed.")

class BlockedDoor(Door):
    def __init__(self):
        super().__init__(self)

    def open_door(self):
        print("The blocked door cannot be opened.")

    def close_door(self):
        print("The blocked door cannot be closed.")

my_door = Door("Opened")
my_door.open_door()
my_door = BlockedDoor()
my_door.open_door()

'''ENCAPSULATION, POLYMORPHISM AND MORE'''

'''Exercise 4:

Analyse the code below before executing it. What will be the output ? Why ?

class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis() '''

#The output will be "doing this in A". That happens because B is before C in the class definition, and since B is a child
# class of A, it'll inherit its method "dothis".

'''Exercise 5:

Analyse the code below before executing it. What will be the output ? Why ?

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)'''

# Woow this is an awesome book - because foundation instance was passed with True parameter
# Title: Asimov - Because this is the first parameter specified when passing the instance
# 5£ - Price input by user
# False - Because is_awesome parameter was given as True, so self.bored is False
# I am very bored - because boring_book instance was passed as False, so is_awesome is False and self.bored is True
# True - Because is_awesome parameter was given as False, so self.bored is True

