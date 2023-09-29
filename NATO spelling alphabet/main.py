dict = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

letter_low = input("Write Letters or World what you need to pronounce:")
letter_upper = letter_low.upper()
letter_count = len(letter_upper)

print(letter_count)

for i in range(letter_count):
    if letter_upper in dict:
        value = dict[letter_upper]
        print(f"The value for {letter_low} is {value}")



# else:
#     print(f"{key_to_find} not found in the dictionary")