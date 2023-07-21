# Example list of letters
letters = ['a', 'b', 'c', 'd', 'e']

while True:
    # Take input letter from user
    input_letter = input("Enter a letter: ")

    # Initialize loop variable
    found = False

    # Iterate through list using a while loop
    i = 0
    while i < len(letters):
        if letters[i] == input_letter:
            found = True
            break
        i += 1

    # Check if letter was found and print result
    if found:
        print(f"{input_letter} is present in the list.")
    else:
        print(f"{input_letter} is not present in the list.")

    # Ask user if they want to continue searching for letters
    answer = input("Do you want to continue searching? (y/n): ")
    if answer.lower() == "n":
        break