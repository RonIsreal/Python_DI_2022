from translate import Translator

translator = Translator("en-US")

french_words = ["bonjour", "au revoir", "Bienvenue", "a bientôt"]
translated_words = []
mydict = {}

for word in french_words:
    lang_to_en = translator.translate(word)
    translated_words.append(lang_to_en)

for i in range(len(french_words)):
    mydict[french_words[i]] = translated_words[i]
print(mydict)
print(translated_words)