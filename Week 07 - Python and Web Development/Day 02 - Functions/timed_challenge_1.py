
def find_occurences():
    sentence = input("Please write a sentence: ")
    user_char = input("Please choose a letter: ")
    count = sentence.count(user_char)
    print(f'Sentence: "{sentence}"\nLetter: "{user_char}"\nCount: {count}')

find_occurences()
