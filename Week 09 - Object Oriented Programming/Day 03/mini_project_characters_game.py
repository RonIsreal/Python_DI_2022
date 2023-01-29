class Character:

    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other_char):
        other_char.life -= self.attack

    @staticmethod
    def clash_result(char1, char2):
        print(
            f"Result:\n\t{char1.name}: Life: {char1.life} / Attack: {char1.attack}\n\t{char2.name}: Life: {char2.life} / Attack: {char2.attack}")


class Templar(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"The one chosen by the gods, {self.name} joins the fray.")

    def meditate(self):
        self.attack -= 2
        self.life += 10
        print(f"{self.name} meditates.")
        print(f"{self.name}'s Attack: {self.attack}\nLife: {self.life}.")

    def holy_help(self):
        self.attack += 5
        print(f"{self.name} calls for holy help.")
        print(f"{self.name}'s Attack: {self.attack}.")

    def fight(self, other_char):
        other_char.life -= 0.75 * (self.attack + self.life)
        print(f"{self.name} fights {other_char.name}.")
        Character.clash_result(self, other_char)


class Marauder(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"With an iron fist and heart of stone, {self.name} stomps onto the battlefield.")

    def brawl(self, other_char):
        other_char.attack -= 2 * self.attack
        self.life += 0.5 * self.attack
        print(f"{self.name} brawls with {other_char.name}.")
        Character.clash_result(self, other_char)

    def train(self):
        self.life += 2
        self.attack += 2
        print(f"{self.name} buffs himself.")
        print(f"{self.name}'s Attack: {self.attack}\nLife: {self.life}.")

    def roar(self, other_char):
        other_char.attack -= 3
        print(f"{self.name} roars on {other_char.name}.")
        Character.clash_result(self, other_char)


class Necromancer(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"With unlimited curiosity and thirst for power, {self.name} curses the land.")

    def curse(self, other_char):
        other_char.attack -= 2
        print(f"{self.name} curses {other_char.name}.")
        Character.clash_result(self, other_char)

    def summon(self):
        self.attack += 3
        print(f"{self.name} summons the undead.")
        print(f"{self.name}'s Attack: {self.attack}.")

    def cast_spell(self, other_char):
        other_char.attack -= self.attack / self.life
        print(f"{self.name} cast a spell on {other_char.name}.")
        Character.clash_result(self, other_char)


templar = Templar("Gravicius")
marauder = Marauder("Greust")
necromancer = Necromancer("Myrianna")
necromancer.summon()
templar.meditate()
necromancer.curse(templar)