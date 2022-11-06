'''Exercises 1, 2 and 3:

Create a variable called birthdays. Its value should be a dictionary.
Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary,
the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
Ask the user to give you a person’s name and store the answer in a variable.
Get the birthday of the name provided by the user.
Print out the birthday with a nicely-formatted message.

Before asking the user to input a person’s name print out all of the names in the dictionary.
If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
Ask the user for a person’s name – store it in a variable.
Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
Now add this new data into your dictionary.
Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.
'''

birthdays = {
  'lena': '1985/10/19',
  'max': '2021/3/15',
  'may': '1982/11/3',
  'gabriel': '1991/5/21',
  'michel': '1993/9/19'
}
new_name = input("Please write the name of the person you would like to add: ").lower()
new_bday = input("Please write the person's birthday using the format 'YYYY/M/D': ")
birthdays[new_name] = new_bday

for users in birthdays:
  print(users)
print("Welcome! You can look for someone's birthday.")
user_input = input("Please write the person's name: ").lower()
for name, date in birthdays.items():
  if user_input in name:
    print(f"{name}'s birth date was on {date}.")
    
'''Exercise 4:

Create a new dictionary called items and populate the dictionary with the following key value pairs, each pair represents an item and its price.

    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3


Print all the items and their prices in a sentence.

Change the value of all the keys to dictionaries containing both the price and the amount of items in stock.
Once you’ve added the stock details write some code to calculate how much it would cost to buy everything in stock.
'''

items = {
  'banana': {'price': 4, 'amount': 10},
  'apple': {'price': 2, 'amount': 10},
  'orange': {'price': 1.5, 'amount': 4},
  'pear': {'price': 3, 'amount': 2}
}

total_cost = 0
for k, v in items.items():
  print(f"{k} for only ${v['price']}! Quick! There are only {v['amount']} units left!")
  sum_total = v['price']*v['amount']
  total_cost += sum_total
print(total_cost)

'''Exercise 5:

Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
Convert it into a list using Python (don’t do it by hand!).
Print out a message saying how many manufacturers/companies are in the list.
Print the list of manufacturers in reverse/descending order (Z-A).
Using loops or list comprehension:
Find out how many manufacturers’ names have the letter ‘o’ in them.
Find out how many manufacturers’ names do not have the letter ‘i’ in them.

Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
Remove these programmatically. (Hint: you can use sets to help you).
Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”),
also print out a message saying how many companies are now in the list.

Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
'''

cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
car_list = list(cars_string.split(","))
print(f"There are {len(car_list)} manufacturers in the list.")
sorted(car_list, reverse = True)
print(car_list)

o_count = 0
i_count = 0

for car in car_list:
    if 'o' in car:
      o_count += 1
for car in car_list:
    if 'i' not in car:
        i_count += 1

print(f"{o_count} manufacturers' names contain the letter 'o'.")
print(f"{i_count} manufacturers' names doesn't have the letter 'i'.")

dup_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
clear_list = list(set(dup_list))
print(f"There are now {len(clear_list)} manufacturers in the list. The manufacturers are: {clear_list}.")
list_sort = sorted(clear_list)
for manuf in list_sort:
  print(manuf[::-1])
            
        
    

