# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if len(names) == 0:
    print("No names entered. Exiting...")
    exit()
elif len(names) == 1:
    print(names[0] + "Is going to have a lonely meal today!")
else:
    print(random.choice(names) + " is going to buy the meal today!")

