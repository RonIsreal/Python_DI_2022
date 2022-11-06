'''Exercise 1 : Family
Instructions
Create a class called Family and implement the following attributes:

members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
last_name : (string)
Initial members data:

[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
Implement the following methods:

born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
family_presentation: a method that prints the family’s last name and all the members’ first name.'''

class Family:

    def __init__(self, last_name):
        # self.name = name
        # self.age = age
        # self.gender = gender
        # self.is_child = is_child
        self.last_name = last_name
        self.members = [{'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}]

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations {self.last_name} family for your newest member, {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    return True
                else:
                    return False

    def family_presentation(self):
        # first_names = []
        # for members in self.members:
        #     first_names.append(members['name'])
        first_names = [member['name'] for member in self.members]
        print(f"The {self.last_name} family is composed currently by {first_names}")

testfamily = Family('Verona')
testfamily.born(name ='Max', age = 0, gender = 'Male', is_child = True)
print(testfamily.is_18('Max'))
print(testfamily.is_18('Michael'))
testfamily.family_presentation()

'''Exercise 2 : TheIncredibles Family
Instructions
Create a class called TheIncredibles. This class should inherit from the Family class:

This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
Initial members data:

[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


4. Call the incredible_presentation method.
5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
6. Call the incredible_presentation method again.'''

class TheIncredibles(Family):
    
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

    def use_power(self):
        for member in self.members:
            if member['age'] >= 18:
                print(f"{member['name']} -> {member['power']}")
            else:
                raise Exception(f"Family member {member['name']} is not old enough to use its powers.")

    def incredible_presentation(self):
        # names_powers = [member['incredible_name'] for member in self.members]
        # powers_names = [member['power'] for member in self.members]
        # names_and_powers = [[name, power] for name, power in zip(names_powers, powers_names)]
        # print(names_and_powers)
        # OR
        testpowers = [[member['incredible_name'], member['power']] for member in self.members]
        print(testpowers)


powerfamily = TheIncredibles("StrongOnes")
# powerfamily.incredible_presentation()
# powerfamily.born(name ='Jack', age = 0, gender = 'Male', is_child = True, power = 'unknown power', incredible_name = 'Baby Jack')
powerfamily.incredible_presentation()
# print(powerfamily.use_power())



