# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
first_digit = int(position[0])
second_digit = int(position[1])

map[second_digit-1][first_digit-1] = "X"

# if second_digit == 1:
#     row1[first_digit-1] = " X"
# if second_digit == 2:
#     row2[first_digit-1] = " X"
# if second_digit == 3:
#     row3[first_digit-1] = " X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
