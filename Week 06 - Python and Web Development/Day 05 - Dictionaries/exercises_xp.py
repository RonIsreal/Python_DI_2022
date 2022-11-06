'''Exercise 1:

Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys, values)))

'''Exercise 2:

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


How much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable
(Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
'''

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for name, age in family.items():
    total_price = 0
    for age in family:
        if age is 0:
            break
        elif age in range(0,3):
            pass
        elif age in range(3,13):
            total_price += 10
        else:
            total_price += 15
print(total_price)

#Bonus resolution

family_dict = {}

new_order = input("Would you like to order tickets? (Yes/No)")

while new_order.lower() == 'yes':
  name = input("Please write the person's name: ")
  family_dict[name] = int(input("Please write the person's age: "))
  new_order = input("Would you like to add more people? (Yes/No)")
  
    
print(family_dict)


total_price = 0

for k, v in family_dict.items():
  if v is 0:
    break
  elif v in range(0,3):
    print(f"{k} doesn't need to pay.")
    pass
  elif v in range(3,13):
    print(f"{k} has to pay $10 for his/her ticket.")
    total_price += 10
  else:
    print(f"{k} has to pay $15 for his/her ticket.")
    total_price += 15
print(f"The total price will be ${total_price}.")

'''Exercise 3:

1. Here is some information about a brand.
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green
    
2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
3. Change the number of stores to 2.
4. Print a sentence that explains who Zaras clients are.
5. Add a key called country_creation with a value of Spain.
6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
7. Delete the information about the date of creation.
8. Print the last international competitor.
9. Print the major clothes colors in the US.
10. Print the amount of key value pairs (ie. length of the dictionary).
11. Print the keys of the dictionary.
12. Create another dictionary called more_on_zara with the following details:

creation_date: 1975 
number_stores: 10 000


13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
14. Print the value of the key number_stores. What just happened ?
'''

#2 
brand = {
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women", "children", "home"], 
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000, 
    "major_color": { 
        "France": "blue", 
        "Spain": "red", 
        "US": {"pink", "green"}
    }
      
}
#3
brand['number_stores'] = 2

#4
print("Zara has a very diversified range of customers all over the world.")

#5
brand['country_creation'] = "Spain"

#6
for k, v in brand.items():
  if k == 'international_competitors':
    brand['international_competitors'].append("Desigual")
    
#7
del brand['creation_date']

#8
print(brand['international_competitors'][-1])

#9
print(brand['major_color']['US'])

#10
print(len(brand))

#11
print(brand.keys())

#12
more_on_zara = {
  'creation_date': 1975, 
  'number_stores': 10000
}

#13
brand.update(more_on_zara)
print(brand)

#14
print(brand['number_stores'])
# The number of stores was updated to 10000.

'''Exercise 4:

Use this list :

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


#4/ Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#5/ Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
#6/ Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#7/ Only recreate the 1st result for:
#7.1/ The characters, which names contain the letter “i”.
#7.2/ The characters, which names start with the letter “m” or “p”.
'''

users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
numbers = list(range(0,5))

#1
disney_users_A = dict(zip(users, numbers))
print(disney_users_A)

#2
disney_users_B = dict(zip(numbers, users))
print(disney_users_B)

#3
disney_users_C = dict(zip(sorted(users), numbers))
print(disney_users_C)

#4
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
numbers = list(range(0,5))
disney_users = {}
for user, number in zip(users, numbers):
  disney_users[user] = number
print(disney_users)

#5
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
numbers = list(range(0,5))
disney_users = {}
for number, user in zip(numbers, users):
  disney_users[number] = user
print(disney_users)

#6
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
sorted_users = list(sorted(users))
numbers = list(range(0,5))
disney_users = {}
for user, number in zip(sorted_users, numbers):
  disney_users[user] = number
print(disney_users)

#7.1
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
numbers = list(range(0,5))
disney_users_A = dict(zip(users, numbers))
print(disney_users_A)

for user, number in disney_users_A.items():
  for letter in user:
    if letter.lower() == 'i':
      print(user)

#7.2
for user, number in disney_users_A.items():
  if user.startswith("M"):
    print(user)
  elif user.startswith("P"):
    print(user)


    




            
    
