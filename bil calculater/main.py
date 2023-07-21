# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Refer to the flow chart here: https://bit.ly/36BjS2D

divided_by_4 = year / 4
divided_by_100 =  year / 100
divided_by_400 = year / 400

remainder_by_4 = (divided_by_4).is_integer()
remainder_by_100 = (divided_by_100).is_integer()
remainder_by_400 = (divided_by_400).is_integer()

if remainder_by_4 == True and remainder_by_100 == True and remainder_by_400 == True:
    print("Leap")
if remainder_by_4 == True and remainder_by_100 == True and remainder_by_400 == False:
    print("NOT Leap")
if remainder_by_4 == True and remainder_by_100 == False:
    print("Leap")
if remainder_by_4 == False:
    print("NOT Leap")
