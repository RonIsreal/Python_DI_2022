'''Exercise 2 : Dungeons & Dragons
Instructions
For a game of Dungeons & Dragons, each player starts by generating a character they can play with. This character has, among other things, six attributes/stats:
Strength
Dexterity
Constitution
Intelligence
Wisdom
Charisma

These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and record the sum of the largest three dice. You do this six times, once for each ability.
For example, the six throws of four dice may look like:
5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.

Create a class called Character and a class called Game for this exercise.

The point of this exercise is to generate characters for players looking to start a game quickly.
Start by asking the user how many players are playing.
Each user then creates his/her character, let them establish what the characters name and age are.
Output the characters created into the following formats:
txt: a nicely formatted text file for the players to use
json: a json file of all the characters and attributes


Hint: the Character class should be in charge of creating characters, the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt'''

import random
import json

class Character:

    def __init__(self):
        self.name = input("Please choose your name: ")
        self.age = int(input("Please choose your age: "))
        self.characters = {}
        self.attributes = self.get_attributes()

    def get_rolls(self):
        # generates 4 dice rolls and eliminates the lowest value. Then sum the remaining 3 values
        rolls = 4
        sum_total = 0
        for i in range(1,rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            die3 = random.randint(1,6)
            die4 = random.randint(1,6)
        dice = [die1, die2, die3, die4]
        dice.remove(min(dice))
        sum_total += sum(dice)
        return sum_total

    def get_attributes(self):
        # run the get_rolls method in order to obtain the value for each attribute, then it assigns it to them
        char_attributes = {'strength': 0, 'dexterity': 0, 'constitution': 0, 'ingelligence': 0, 'wisdom': 0, 'charisma': 0}
        for attributes in char_attributes:
            char_attributes[attributes] = self.get_rolls()
        print(f"Valiant warrior {self.name.capitalize()}, born {self.age} winters ago! This is your current power! {char_attributes}")

    def __str__(self):
        return f"This is you: {self.name}, {self.age}, {self.attributes}"


class Game:

    def __init__(self):
        self.player_count = int(input("Please choose how many players will participate: "))
        self.players = []
        self.create_character()
        # self.save_characters()

    def create_character(self):
        for i in range(0,self.player_count):
            player = Character()
            self.players.append(player)
        print(self.players.__str__())

    def save_characters(self):
        with open('charactersdnd.json', 'w') as f:
            json.dump(self.players, f, indent=3)



test = Game()
print(test.players)