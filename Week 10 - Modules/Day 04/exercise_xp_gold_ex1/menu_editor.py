import menu_manager

def load_manager():
    global newuser
    newuser = menu_manager.MenuManager()
    user_name = input("Please write your name: ")
    print(f"User Created\nHello {user_name}, please select from the menu below.\n")
    show_user_menu()
    return newuser


def show_user_menu():
    user_choice = input("    MENU\n(a) ADD an item\n(d) DELETE an item\n(v) VIEW the menu\n(x) EXIT\n-> ").lower()
    if user_choice == 'a':
        name = input("Please write the item's name: ")
        price = float(input("Please write the item's price: "))
        newuser.add_item(name, price)
        show_user_menu()
    elif user_choice == "d":
        item_name = input("Please write which item you would like to delete: ")
        newuser.remove_item(item_name)
        show_user_menu()
    elif user_choice == "v":
        newuser.show_restaurant_menu()
        show_user_menu()
    elif user_choice == "x":
        newuser.save_to_file()
        print("Closing the Program.")
    else:
        print("Not a valid input")
        show_user_menu()


load_manager()
