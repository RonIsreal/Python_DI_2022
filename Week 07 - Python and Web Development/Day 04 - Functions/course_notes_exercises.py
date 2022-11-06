'''Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious string inside the list.'''

def sum_numbers(*args):
    args = [item for item in args if isinstance(item, int)]
    print(sum(args))

sum_numbers(2,3,1,2,"four",42,1,5,3,"imanumber")

'''Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters'''

def say_hello(str):
    print(f"Hello, {str}!")

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_people = filter(lambda name: len(name) <= 4, people)
list(map(say_hello, filtered_people))