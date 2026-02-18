import string

text = input("Enter a sentence: ")

text = text.lower()

alphabet = set(string.ascii_lowercase)

if alphabet.issubset(set(text)):
    print("The given string is a Pangram.")
else:
    print("The given string is NOT a Pangram.")
