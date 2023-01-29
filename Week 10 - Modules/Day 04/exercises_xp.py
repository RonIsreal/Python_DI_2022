'''Exercise 1 – Random Sentence Generator
Instructions
Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

Hint : The generated sentences do not have to make sense.

Download this word list

Save it in your development directory.

Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
use the words list to get your random words.
the amount of words should be the value of the length parameter.

Take the random words and create a sentence (using a python method), the sentence should be lower case.

Create a function called main which will:

Print a message explaining what the program does.

Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
If the user inputs incorrect data, print an error message and end the program.
If the user inputs correct data, run your code.'''

import random
random.seed()

words_list = []
# def get_words_from_file():
#
#
#     sentence_length = int(input("Please choose a length for your sentence. It should be between 2 and 20 words only: ")) -1
#     f = open("sowpods.txt", "r")
#     words = f.readlines()
#     for word in words:
#         if sentence_length not in range(2,20):
#             print("The length provided is invalid.")
#             break
#         else:
#             while len(words_list) <= sentence_length:
#                 words_list.append(random.choice(words))
#
#
# get_words_from_file()
# print(words_list)

def main():

    print("This small program will generate a random sentence based on the length chosen by the user. The sentence most likely won't make any sense!")

    global sentence_length
    sentence_length = int(input("Please choose the length of your sentence. It should be a value between 2 and 20: "))
    if sentence_length in range(2,21):
        get_words_from_file()
        get_random_sentence()
        generate_sentence()
    else:
        print("The value you chose is invalid. Closing...")

def get_words_from_file():

    f = open("sowpods.txt", "r")
    words = f.readlines()
    for word in words:
        words_list.append(word)

def get_random_sentence():

    global chosen_words
    chosen_words = []
    while len(chosen_words) <= sentence_length -1:
        chosen_words.append(random.choice(words_list).lower())
    # random_sentence = "".join(chosen_words)
    # print(random_sentence)

def generate_sentence():
    random_sentence = " ".join(chosen_words)
    print(random_sentence)
main()

'''Exercise 2: Working With JSON
Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file.'''

import json
sampleJson = {
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}
print(sampleJson['company']['employee']['payable']['salary'])
sampleJson["company"]["employee"]["birth_date"] = "20/07"
with open('result.json', 'w') as f:
    json.dump(sampleJson, f)
