from key_value import DictSearch

morse_code_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                       "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                       "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", ".--": "w", "-..-": "x", "-.--": "y",
                       "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
                       "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-.-.-": ".", "--..--": ","}

# to search for a key by its value
search = DictSearch(my_dict=morse_code_alphabet)

# Users input
search_value = input("Enter ").lower()

# Break a string into individual letters
letters = [letter for letter in search_value]
print(letters)

empty = []

# combining letters
for letter in letters:
    key = search.get_key_by_value(search_value=letter)
    empty.append(key)

final_code = " ".join(empty)
print(final_code)
