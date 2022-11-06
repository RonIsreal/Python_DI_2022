'''Exercise 1: Cats

Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.'''

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_one = Cat("Pank", 7)
cat_two = Cat("Neko", 5)
cat_three = Cat("Banzai", 6)

def find_oldest():
    oldest = max(cat_one, cat_two, cat_three, key=lambda cat: cat.age)
    print(f"The oldest cat is {oldest.name}. He is {oldest.age}.")

find_oldest()

'''Exercise 2 : Dogs
Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.'''


class Dogs:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes Woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height}cm high!")


davids_dog = Dogs("Rex", 50)

print(f"David has a dog. His dog's name is {davids_dog.name} and he is {davids_dog.height} tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dogs("Teacup", 20)

print(f"Sarah has a dog. Her dog's name is {sarahs_dog.name} and he is {sarahs_dog.height} tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")

'''Exercise 3: Who’s The Song Producer?
Instructions
Define a class called Song, it will show the lyrics of a song.
Its __init__() method should have two arguments: self and lyrics (a list).
Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
Create an object, for example:

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


Then, call the sing_me_a_song method. The output should be:

There’s a lady who's sure
all that glitters is gold
and she’s buying a stairway to heaven'''


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for items in self.lyrics:
            print(items)


stairway = Song(["There’s a lady who's sure", "All that glitters is gold", "And she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

'''Exercise 4: Afternoon At The Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)'''

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal.lower() in self.animals:
            print("This animal already exists.")
        else:
            new_animal = self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self,sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
        else:
            print("You don't have the specified animal.")

    def sort_animals(self):
        self.animals = sorted(["Ape", 'Cat', 'Cougar', "Baboon", "Bear", 'Eel', 'Emu'])
        s = {}
        differentLetters = sorted(list(set(map(lambda x: x.lower()[0], self.animals))))
        for animal in self.animals:
            firstLetter = animal.lower()[0]
            pos = differentLetters.index(firstLetter) + 1
            try:
                s[pos].append(animal)
            except KeyError:
                s.update({pos: []})
                s[pos].append(animal)
        print(s)


ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('zebra')
ramat_gan_safari.add_animal('horse')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('horse')
ramat_gan_safari.sell_animal('chicken')
ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal('hippo')
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()

