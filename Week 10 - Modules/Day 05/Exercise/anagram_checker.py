import string


class AnagramChecker:

    def __init__(self):
        self.wordlist = []
        self.word_anagrams = []
        self.open_file()

    def open_file(self):
        with open('sowpods.txt') as f:
            self.wordlist = [line.strip() for line in f]
            return


    def is_valid_word(self, word1):
       print(word1)
       if word1.isalpha():
           self.is_anagram(word1)
       else:
           print("Please write a single word without empty spaces or digits.")
           self.is_valid_word()


    def is_anagram(self, word1):
        for item in self.wordlist:
            if (sorted(word1) == sorted(item)):
                self.word_anagrams.append(item)
            self.get_anagrams()
            return True
        else:
            return False

    def get_anagrams(self):
        print(f"These are your anagrams: {self.word_anagrams}")



test = AnagramChecker()
test.is_valid_word("zaaz")