'''Create a Door class, it has only the following attributes:
id (int) : An id number, use a class variable objs that counts how many door have been created so far and use this number as the id of the door.
locked (boolean)
next (List of Door obs) : The next doors available from this one

Create a method can_go_to(self, other_door) in the Door class that checks if the path from this door to other_door can be made (the locked doors cannot be opened !).

Bonus: Display the path
Bonus 2: Add an integer variable KEYS that holds a limited number of keys available to open locked doors (each key can be used only once).
'''

class Door:

    door_count = 0

    def __init__(self, name):

        Door.door_count += 1
        self.name = name
        self.id_number = Door.door_count
        self.locked = True
        self.next = []
        self.keys = 0

    def can_go_to(self, other_door):
        if other_door.locked == False:
            print(f"Can go to door {other_door.name}. {self.door.name} led you to {other_door.name}.")
        else:
            print(f"{other_door.name} is locked.")

    def get_keys(self, keycount):

        self.keys += keycount
        print(f"You have acquired {keycount} keys.")

    def unlock_door(self, other_door):

        while self.keys > 0:
            if other_door.locked == True:
                self.keys -= 1
                other_door.locked == False
                print(f"You used a key. You have {self.keys} keys left.")
                break
            else:
                print(f"{other_door.name} is already unlocked.")
                break
        else:
            print(f"You have no keys left. KEYS: {self.keys}")


door1 = Door('MyDoor')
door2 = Door('NextDoor')
door1.can_go_to(door2)
door1.get_keys(2)
door1.unlock_door(door2)
print(door2.locked)
door1.can_go_to(door2)