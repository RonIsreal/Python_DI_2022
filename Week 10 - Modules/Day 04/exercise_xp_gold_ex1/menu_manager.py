import json

class MenuManager:

    def __init__(self):
        self.menu = self.open_menu()


    def open_menu(self):
        # Opens the JSON file and convert it into a single dictionary, making it easier to work with and append it to the self.menu variable
        # from the class
        with open("restaurant_menu.json", "r+") as f:
            self.menu = {entry["name"]: entry["price"] for entry in json.load(f)["items"]}
        return self.menu

    def show_restaurant_menu(self):
        # Prints the menu line by line
        for key, value in self.menu.items():
            print(f"{key}: ${value}")

    def add_item(self, name, price):
        # Adds the provided key and value to the self.menu dictionary. If it already exists, it replaces the value only
        self.menu[name] = price
        print(self.menu)

    def remove_item(self, item_name):
        # Checks if the key provided by item_name exists and it deletes it in case it's True
        for items in self.menu:
            if self.menu.get(item_name):
                del self.menu[item_name]
                print(f"The item {item_name} was removed successfully from the menu.")
                print(True, self.menu)
                return
            else:
                print(f"The item {item_name} isn't on the menu.")
                print(False)
                return
        print(self.menu)

    def save_to_file(self):
        # Convert the file back to its original format and write it back to the JSON file
        self.menu = {'items': [
            {"name": name,
             "price": price
            } for name, price in self.menu.items()]}
        print(self.menu)
        with open("restaurant_menu.json", "w") as f:
            json.dump(self.menu, f, indent=3)
        print("Your changes were saved successfully.")

mn = MenuManager()
print(mn.open_menu())

