class Farm:

	def __init__(self, name):
		self.name = name
		self.animals = {}

	def add_animal(self, name, amount=1):
		if name in self.animals:
			self.animals[name] += amount
		else:
			self.animals[name] = amount

	def get_info(self):
		print(f"{self.name}'s Farm\n")
		for name, amount in self.animals.items():
			print(f"{name} : {amount}")
		print("\n\tE-I-E-I-O!")

	def get_animal_types(self):
		all_animals = []
		for animals in self.animals:
			all_animals.append(animals)
		return(sorted(all_animals))

	def get_short_info(self):
		animals_list = self.get_animal_types()
		print(f"McDonald's Farm has {animals_list} ")



mcdnld = Farm("MacDonald")
mcdnld.add_animal("Cow", 5)
mcdnld.add_animal("Sheep")
mcdnld.add_animal("Sheep")
mcdnld.add_animal("Goat", 12)
mcdnld.get_info()
mcdnld.get_short_info()