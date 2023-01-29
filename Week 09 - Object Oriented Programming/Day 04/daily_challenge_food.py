'''Instructions :
Create a Person class which will have three properties:
Name
List of foods they like
List of foods they hate
Note: A person can have an empty list for foods they hate and/or love.

In this class, create the method taste():
It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person’s like list, add ‘and loves it!’ to the end.
If it is in the person’s hate list, add ‘and hates it!’ to the end.
If it is in neither list, simply add an exclamation mark to the end.'''

class Person:

    def __init__(self, name):
        self.name = name
        self.likedfoods = []
        self.hatedfoods = []

    def taste(self, food):

        food_lower = food.lower()
        if food_lower in self.likedfoods:
            print(f"{self.name} tasted {food_lower} and loved it!")
        elif food_lower in self.hatedfoods:
            print(f"{self.name} tasted {food_lower} and hated it!")
        else:
            print(f"{self.name} tasted {food_lower}!")

    def likesfood(self):
        food_item = input("Please write all the foods you like separated by comma: ").split(",")
        for item in food_item:
            self.likedfoods.append(item)
        print(f"The following food were added to your liked foods list: {food_item}")
        print(self.likedfoods)

    def hatesfood(self):
        hfood_item = input("Please write all the foods you dislike separated by comma: ").split(",")
        for item in hfood_item:
            self.hatedfoods.append(item)
        print(f"The following food were added to your liked foods list: {hfood_item}")
        print(self.hatedfoods)




ron = Person("Ronny")
ron.likesfood()
ron.hatesfood()
ron.taste('FISH')
ron.taste('chocolate')
ron.taste('AVOCADO')
