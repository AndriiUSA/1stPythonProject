# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

low_score_names = name1.lower() + name2.lower()
t = low_score_names.count('t')
r = low_score_names.count('r')
u = low_score_names.count('u')
e = low_score_names.count('e')
true = t + r + u + e
l = low_score_names.count('l')
o = low_score_names.count('o')
v = low_score_names.count('v')
e = low_score_names.count('e')

love = l + o + v + e
love_score  = str(true) + str(love)
love_int = int(love_score)
if love_int < 10 or love_int > 90:
    print("Your score is " + (love_score) +", you go together like coke and mentos.")
elif love_int > 40 and love_int <50:
    print("Your score is " + (love_score) +", you are alright together.")
else:
    print("Your score is " + (love_score) + ".")
