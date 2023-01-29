'''Exercise 1 : Regular Expression #1
Instructions
Hint: Use the RegEx (module)

Use the regular expression module to extract numbers from a string.

Example

return_numbers('k5k3q2g5z6x9bn')
// Excepted output : 532569'''

import re
import random
import string

my_string = 'k5k3q2g5z6x9bn'
str_numbers = re.findall(r'\d+', my_string) #\d is the RegEx for Unicode decimal digits
print(str_numbers)

'''Exercise 2 : Regular Expression #2
Instructions
Hint: Use the RegEx (module)

Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
The name should contain only letters.
The name should contain only one space.
The first letter of each name should be upper cased.'''

user_name = input("Please write your full name: ")
user_name_match = re.match(r'^[A-Z]{1}[a-z]{1,}\s?[A-Z]{1}[a-z]{1,}$', user_name) #RegEx breakdown -> ^: string starting point, \s?: Max 1 white spate

if user_name_match:
    print("Only letters")
else:
    print("Contain invalid characters.")


'''Create a Python program that will generate a good password for you.

Program flow:

Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter a valid one.

Generate a password with the required length.

Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

Rules for the validity of the password

Each password should contain:
At least 1 digit (0-9)
At least 1 lower-case character (a-z)
At least 1 upper-case character (A-Z)
At least 1 special character (eg. !, @, #, $, %, ^, _, …)
Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

Create a test function first!

Do the following steps 100 times, with different password lengths:
Generate a password.
Test the password to ensure that:
it fulfills all the requirements above (eg. it has at least one digit, etc.)
it has the specified length.'''

# "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,30}$"
characters = string.ascii_letters + string.digits + string.punctuation

def generate_pw():
    pwlen = int(input("Please choose the length of your desired password (Minimum 6 and Maximum 30 characters long): "))
    if pwlen in range(6,31):
        randompw = "".join(random.choice(characters) for i in range(pwlen))
        pwmatch = re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,30}$", randompw)
        if pwmatch:
            print(f"This is your generated password: {randompw} . Keep it in a safe place and don't share it with anyone!")
        else:
            print(randompw)
            print("Not quite.")
            generate_pw()
    else:
        generate_pw()
generate_pw()