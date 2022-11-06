'''Exercise:

In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.

Create a python program that encrypts and decrypts messages with ceasar cypher,
the user entries the program, and then the program asks him if he wants to encrypt or decrypt,
and then execute encryption/decryption on a given message and a given shift.
'''

import string

def encript():

    text = list(input("Please paste the text you would like to encrypt: "))
    number = int(input("Please specify the shift value: "))
    cypher_text = ""
    for letter in text:
        cypher_text += chr(ord(letter) - number) #The chr() function returns a character according to its unicode value. As for the ord() function it returns a character's unicode value. 
    print(str(cypher_text))

def decript():
    
    text = list(input("Please paste the text you would like to encrypt: "))
    number = int(input("Please specify the shift value: "))
    cypher_text = ""
    for letter in text:
        cypher_text += chr(ord(letter) + number)
    print(str(cypher_text))
    
user_input = input("Please specify if you would like to 'encript' or 'decript' a message: ").lower()

if user_input == 'encript':
    encript()
elif user_input == 'decript':
    decript()
else:
    print("Invalid input.")
