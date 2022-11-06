'''Exercise 1:

Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


Create another cat breed named Siamese which inherits from the Cat class.
Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
Those three cats are Sara’s pets. Create a variable called sara_pets whose value is an instance of the Pet class, and pass the variable all_cats to the new instance.
Take all the cats for a walk, use the walk method'''

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


chartreux_cat = Chartreux("Cedric", 3)
siamese_cat = Siamese("Gizmo", 1)
bengal_cat = Bengal("Tiger", 5)
all_cats = [chartreux_cat, siamese_cat, bengal_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()
print(bengal_cat.sing("Roar"))

'''Exercise 2 : Dogs

Instructions

Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter whose value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with 
the higher run_speed x weight.

Create 3 dogs and run them through your class.'''

class Dog():

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking!")

    def run_speed(self):
        dog_speed = (self.weight / self.age) * 10
        return dog_speed

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} won the fight.")
        elif self.run_speed() == other_dog.run_speed():
            print(f"Draw!")
        else:
            print(f"{other_dog.name} won the fight.")


# dog_luna = Dog("Luna", 8, 35)
# dog_alfred = Dog("Alfred", 17, 9)
# dog_riki = Dog("Riki", 11, 30)
# dog_luna.fight(dog_alfred)
# dog_alfred.fight(dog_riki)
# dog_riki.fight(dog_riki)

