'''Exercise 1 : What’s Your Name ?
Instructions
Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.'''

def get_full_name(first_name, last_name, middle_name = None):
    if middle_name is not None:
        print(f"{first_name} {middle_name} {last_name}")
    else:
        print(f"{first_name} {last_name}")

get_full_name("Ronny", "Edelstein")
get_full_name("Lena", "Zilberberg", "Edelstein")

'''Exercise 2 : From English To Morse
Instructions
Write a function that converts English text to morse code and another one that does the opposite.
Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.'''

english_to_morse = {'a':"*-", "b":"-***", "c":"-*-*", "d":"-**", "e":"*", "f":"**-*", "g":"--*", "h":"****", "i":"**", "j":"*---", "k":"-*-", "l":"*-**", "m":"--", "n":"-*", "o":"---", "p":"*--*", "q":"--*-", "r":"*-*", "s":"***", "t":"-", "u":"**-", "v":"***-", "w":"*--", "x":"-**-",
                    "y":"-*--", "z":"--**", "0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****", "7": "--***", "8": "---**", "9": "----*",
                    ".": "*-*-*-", ",": "--**--", ":": "---***", "?": "**--**", "'": "*----*", "/": " "}
morse_to_english = {v:k for k,v in english_to_morse.items()}

def translate_eng_to_morse(message):
    encoded_message = ""
    for letter in message:
        if letter.lower() in english_to_morse:
            encoded_message += english_to_morse[letter] + " "
    return encoded_message

print(translate_eng_to_morse("hello/in/morse/code"))

def translate_morse_to_eng(message):
    encoded_message = ""
    for letter in message.split("/"):
        if letter in morse_to_english:
            encoded_message += morse_to_english[letter]+ " "
    return encoded_message

print(translate_morse_to_eng("****/*/*-**/*-**/---/ /**/-*/ /--/---/*-*/***/*/ /-*-*/---/-**/*/"))