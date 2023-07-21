import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

shapes = [rock, paper, scissors]

enter_shape = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n'))

if enter_shape not in range(3):
    print("Invalid input. Please enter a number from 0 to 2.")
else:
    random_shape = random.choice(shapes)
    print(random_shape)

    if enter_shape == shapes.index(random_shape):
        print("It's a draw.")
    else:
        result = (enter_shape - shapes.index(random_shape)) % 3
        if result == 1:
            print("You win! " + shapes[enter_shape] + " beats " + shapes[shapes.index(random_shape)])
        else:
            print("Computer wins! " + shapes[shapes.index(random_shape)] + " beats " + shapes[enter_shape])
