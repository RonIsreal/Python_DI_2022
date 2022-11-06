from exercises_xp import Dog
import random

class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.trained = True
        self.bark()

    def play(self, *args):
        print(f"{self.name}, {args} are all playing together!")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_trick = random.choice(tricks)
        if self.trained:
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not trained.")


dog_luna = PetDog("Luna", 8, 35)
dog_luna.train()
dog_alfred = PetDog("Alfred", 17, 10)
dog_riki = PetDog("Riki", 10, 30)
dog_luna.play(dog_riki.name, dog_alfred.name)
dog_luna.do_a_trick()
dog_riki.do_a_trick()