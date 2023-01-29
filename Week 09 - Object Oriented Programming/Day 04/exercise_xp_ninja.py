'''Exercise 1: Creature
This exercise is inspired by a youtube video from Primer, it tries to simulate natural selection.

Create a class Creature, it has the following attributes:
id (int) Use a class variable
weight (int)
ate_food` (int)

Create a class World, it has the following attributes:
grid (2D list) it represents the ground


3. We will simulate generations of creature fighting for food, at the end of each generation, every creature that ate 1 food will give birth to one baby, each creature that ate more than 1 food will give birth to two, any creature that didn’t find food won’t give birth to any child.


4. During the generation, each creature tries to reach the nearest food, when he reaches it, he eats it, if two creatures reach the same food at the same time, the heaviest one eat it.


5. Create the following methods in the Creature class:
* find_nearest_food(self, grid): grid is the World grid, it returns the coordinate of the nearest food
* next_move(self, grid): it returns the next coordinate of the Creature (it can move only above, below, left and right, not in diagonal)


6. Create the following methods in the World class:
* next_generation(self): Create all the new creatures and start a new generation
* run(self): Run the current generation'''

import pygame
import numpy as np

class Creature:

    count_id = 0

    def __init__(self, weight):

        Creature.count_id += 1
        self.creature_id = Creature.count_id
        self.weight = weight
        self.ate_food = 0
        self.babies = 0

    def find_nearest_food(self, grid):
        pass

    def next_move(self, grid):
        pass

    def eat_food(self):
        pass







class World:

    def __init__(self):
        self.grid = []

    def next_generation(self):
        pass

    def run_generation(self):
        pass

    def creategrid(self, rows = 60, columns = 80):
        pass
