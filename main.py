from playsound import playsound
from key_value import DictSearch

morse_code_alphabet = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                       "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                       "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", ".--": "w", "-..-": "x", "-.--": "y",
                       "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
                       "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-.-.-": ".", "--..--": ","}

# to search for a key by its value
search = DictSearch(my_dict=morse_code_alphabet)

# # Users input
search_value = input("Enter ").lower()
#
# Break a string into individual letters
letters = [letter for letter in search_value]
# print(letters)

empty = []

# combine letters
for letter in letters:
    key = search.get_key_by_value(search_value=letter)
    empty.append(key)


for message in empty:
    sound_letters = [sound_letter for sound_letter in message]
    print(sound_letters)
    if "." in sound_letters:
        for i in range(len(sound_letters)):
            print("True")
            playsound("sounds/dot_morse_code1.mp3")
    if "-" in sound_letters:
        for i in range(len(sound_letters)):
            print("False")
            playsound("sounds/line_morse_code1.mp3")
final_code = " ".join(empty)
print(final_code)

# playsound("sounds/b_morse_code1.mp3")
