def count_occurrences():
    my_string = input("Please write a sentence: ")
    my_letter = input("Please choose a letter between A and Z: ")
    letter_count = 0
    for letters in my_string:
        if my_letter.lower() in letters:
            letter_count += 1
    return letter_count

print(count_occurrences())