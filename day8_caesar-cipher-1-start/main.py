alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'en' to encrypt, type 'de' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_mode):
    result = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_mode == "en":
                new_position = position + shift_amount
            elif cipher_mode == "de":
                new_position = position - shift_amount
            result += alphabet[new_position]
        else:
            result += letter
    if cipher_mode == "en":
        print(f"The encoded text is {result}")
    elif cipher_mode == "de":
        print(f"The decoded text is {result}")
    else:
        print("Invalid mode.")

# Call the caesar() function
caesar(start_text=text, shift_amount=shift, cipher_mode=direction)
