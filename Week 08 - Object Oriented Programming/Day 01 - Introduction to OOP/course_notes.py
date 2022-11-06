'''Exercise 1: Analyse the code below. What will be the ouput ?

Explain the goal of the `__init__()` method'''

class Point():
    def __init__(self, x, y): #Constructor used by Python to initialize the attributes of its class
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x) #p.x is: 3
print("p.y is:", p.y) #p.x is: 4

'''Exercise 2: Analyse the code below. What will be the output ?

Explain the goal of the methods

Create a method that modifies the name of the person'''

class Person(): #Person class with name and age attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self): #Function to display the name assigned to the object person
    print("Hello my name is " + self.name)

  def change_name(self, new_name):
    self.name = new_name

first_person = Person("John", 36) #Call to the function with specified name and age
first_person.show_details() #Hello my name is John

first_person.change_name("Doobie")
first_person.show_details()

'''Exercise 3: Analyse the code below. What will be the output ?'''

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark") #Bad Output, since the main class doesn't have any attributes started or specified
