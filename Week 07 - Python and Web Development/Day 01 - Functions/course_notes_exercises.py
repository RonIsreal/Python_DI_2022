'''Exercise 1:

Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
And also it must return both addition and subtraction in a single return call.
'''

def calculation(a, b):
    
    res_sum = a + b
    res_sub = a - b
    return print(f"The total sum of both values is: {res_sum}.\nThe total subtraction of both values is: {res_sub}.")

calculation(40, 10)

'''Exercise 2:

Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters
'''

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
for name in people:
    if len(name) <= 4:
        print(f"Hello {name}!")
        
# OR
def lower_than_4(name):
    return len(name) <= 4
            
def say_hello(people):
    return people
    print(f"Hello {people}!")
    

filtered_people = filter(lower_than_4, people)
print(list(filtered_people))
map_list = map(say_hello, filtered_people)
print(list(map_list))

