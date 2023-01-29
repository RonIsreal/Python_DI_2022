class Human:

    def __init__(self, id_number, name, age, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.priority = False
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)
        return

    def __str__(self):
        print(f"My family: {self.family}")

class Queue:

    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority == True:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        if person in self.humans:
            return self.humans.index(person)

    def swap(self, person1, person2):
        if person1 and person2 in self.humans:
            p_1_i, p_2_i = self.humans.index(person1), self.humans.index(person2)
            self.humans[p_1_i], self.humans[p_2_i] = self.humans[p_2_i], self.humans[p_1_i]
            return
        else:
            print("One or more people are missing from the list.")
            return

    def get_next(self):
        next_in_line =  self.humans[0]
        self.humans.remove(next_in_line)
        return

    def get_next_blood_type(self, blood_type):
        next_blood = next(blood for blood in self.humans if blood.blood_type == blood_type)
        self.humans.remove(next_blood)
        print(f"Next in line by blood is: {next_blood}.")

    def sort_by_age(self):
        print(f"Sorted line: {sorted(self.humans, key= lambda p: (p.priority, p.age))}")

    def rearrange_queue(self):
        self.sort_by_age()
        for humans in self.humans:
            while humans in range(0, len(self.humans)):
                current_human = self.humans[i]
                next_human = self.humans[i + 1]
                if current_human.family == next_human.family:
                    next_human[i + 1]

    def __str__(self):
        print(f"Humans currently in queue: {self.humans}")




test = Human("12355423", "Xecucleclei", 37, "A")
test2 = Human("fdsfdsf", "Jamaicon", 61, "O")
test3 = Human("dfsdfdsf", "Malakias", 28, "A")
test.add_family_member(test3)
fluvax = Queue()
fluvax.add_person(test)
fluvax.add_person(test2)
fluvax.add_person(test3)
print(str(fluvax.humans))
fluvax.rearrange_queue()
print(str(fluvax.humans))
