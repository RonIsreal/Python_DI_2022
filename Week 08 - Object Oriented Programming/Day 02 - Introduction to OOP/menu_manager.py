'''Exercise 3 : Restaurant Menu Manager
Instructions
The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

Create a python file called menu_manager.py.

Create a class called MenuManager.

Create a method __init__ that instantiates an attribute called menu.
The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name,
price, spice level and gluten index (which value is a boolean).

Here is a list of the dishes currently on the menu:

    Soup – 10 – B - False
    Hamburger – 15 - A - True
    Salad – 18 - A - False
    French Fries – 5 - C - False
    Beef bourguignon– 25 - B - True

    Meaning: For the spice level:
       • A = not spicy,
       • B = a little spicy,
       • C = very spicy


The dishes provided above should be the value of the menu attribute.

Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu,
if the dish exists then update it. If not notify the manager that the dish is not in the menu.

Create a method called remove_item(name). This method should check if the dish is in the menu,
if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.'''

class MenuManager:

    def __init__(self, menu):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        menu_item = dict(name = name, price = price, spice = spice, gluten = gluten)
        self.menu.append(menu_item)

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item['name'] == name:
                item['price'] = price
                item['spice'] = spice
                item['gluten'] = gluten
        else:
            print("This dish is not part of the menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item['name'] == name:
                self.menu.remove(item)
                return
        print(self.menu)


testplate = MenuManager("MyRestaurant")
testplate.add_item("Soup", 10, "B", False)
testplate.add_item("Hamburger", 15, "A", True)
testplate.add_item("Salad", 18, "A", False)
testplate.add_item("French Fries", 5, "C", False)
testplate.add_item("Beef Bourguignon", 25, "B", True)
testplate.update_item("French Fries", 5, "A", False)
print(testplate.menu)
testplate.remove_item("Hamburger")
print(testplate.menu)

