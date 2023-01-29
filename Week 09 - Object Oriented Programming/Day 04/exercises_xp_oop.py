'''Instructions
Create a class Human, it has the following attributes:
name (str)
age (int)
living_place (Building - Default is None)

Create another class Building, it has the following attributes:
address (str)
inhabitants (List of Human objects - Default is empty)

Create a class City, it has the following attributes:
name (str)
buildings (List of Building objects - Default is empty)

Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
Add the construct(self, address) method to the City class, it adds a building at the referenced address.
Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
Created objects and call the methods'''

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.living_place = None #building object (default = None)


    def move(self, building):
        if self.living_place:
            self.living_place.inhabitants.remove(self)
        self.living_place = building
        building.inhabitants.append(self)

    def __repr__(self):
        return f"Person: {self.name}, Age: {self.age}."

class Building:

    def __init__(self, address):
        self.address = address
        self.inhabitants = [] #list of human (class)

    def show_inhabitants_info(self):
        for inhabitant in self.inhabitants:
            print(inhabitant.name, inhabitant.age)

    def remove_inhabitant(self, inhabitant: Human):
        self.inhabitants.remove(inhabitant)

    def get_number_of_inhabitants(self):
        return len(self.inhabitants)

    def get_total_ages_of_inhabitants(self):
        total_ages = 0
        for inhabitant in self.inhabitants:
            total_ages += inhabitant.age
        return total_ages

    def __repr__(self):
        return f"Building in {self.address}. Inhabitants: {self.inhabitants}."

class City:
    def __init__(self, name: str, buildings: list[Building]):
        self.name = name
        self.buildings = buildings
    def construct(self, address):
        new_building = Building(address)
        self.buildings.append(new_building)
    def info(self, address):
        counter = 0
        total_ages_of_humans = 0
        number_of_humans = 0
        for building in self.buildings:
            if building.address == address:
                counter += 1
                number_of_humans += building.get_number_of_inhabitants()
                total_ages_of_humans += building.get_total_ages_of_inhabitants()
        mean = total_ages_of_humans / number_of_humans
        print(f"the number of building at the address {address} is {counter}")
        print(f"the mean age of the citizens at the address {address} is {mean}")
building1 = Building("st")
building2 = Building("bre")
building3 = Building("st")
john = Human("John", 50)
james = Human("James", 65)
alan = Human("Alan", 39)
john.move(building1)
james.move(building1)
alan.move(building3)
tlv = City("Tel Aviv", [building1, building2, building3])
tlv.info("st")