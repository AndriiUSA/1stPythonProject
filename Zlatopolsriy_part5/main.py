# 5.1. Напечатать ряд чисел 20 в виде: 20 20 20 20 20 20 20 20 20 20.
# n = 20
# for i in range(10):
    # print(n, end=' ')

# 5.2. Вывести на экран любое заданное число любое заданное число раз
# n = int(input('Type your number: '))
# for i in range(n):
#     print(n, end=' ')

# 5.3. Напечатать «столбиком»: а) все целые числа от 20 до 35;
# for i in range(20, 36):
#     print(i)
# б) квадраты всех целых чисел от a до 50 (значение a вводится с клавиатуры; a ≤ 50);
# a = int(input('Tape "a" value (should be less than 50): '))
# for i in range(a,51):
#     sqr = i**2
#     print(sqr)

# в) кубы всех целых чисел от 10 до b (значение b вводится с клавиатуры; b ≥ 10);
# b = int(input('Type "b" value (should be more than 10): '))
# for i in range(10, b):
#     cube = i**3
#     print(cube)

# # г) все целые числа от a до b (значения a и b вводятся с клавиатуры; b ≥ a).
# a = int(input('Type "a" value: '))
# b = int(input('Type "b" value (should be more then "a" value): '))
# for i in range(a,b):
#     print(i)

#5.9. Напечатать таблицу перевода расстояний в дюймах в сантиметры для значений 10, 11, ..., 22 дюйма (1 дюйм = 25,4 мм).
# for inch in range(10,23):
#     cm = inch * 2.54
#     print(f'{inch} inches = {cm} centimeters')

#5.10 Напечатать таблицу перевода 1, 2, ... 20 долларов США в грн по текущему курсу (значение курсас клавиатуры).
# exch = float(input('Type exchange rate uah to usd: '))
# for usd in range(1,21):
#     uah = usd * exch
#     print(f'{usd} us dollars = {uah} ukrainian hryvnia')

#5.14. Напечатать таблицу умножения на 9:
# for numb in range(1,10):
#     mult = 9 * numb
#     print(f' 9 x {numb} = {mult}')

# 5.24. Вывести «столбиком» следующие числа: 3,2, 3,2, 3,3, ...,3,9.
# i = 3.2
# while i < 4.0:
#     print(round(i,2))
#     i += 0.1

# 5.25. Вывести «столбиком» следующие числа: 2,2, 2,4, 2,6, ...,4,2.
# n = 2.2
# while n < 4.3:
#     print(round(n,1))
#     n +=0.1
#
# 5.26. Вывести «столбиком» следующие числа: 4,4, 4,6, 4,8, ...,6,4.
# numb = 4.4
# while numb < 6.5:
#     print(round(numb,1))
#     numb +=0.1

# # 5.27. Найти: а) сумму всех целых чисел от 200 до 600;
# sum_of_numbers = 0
# for num in range(200, 600 + 1):
#     sum_of_numbers += num
# print("Sum of numbers in the range:", sum_of_numbers)

# б) сумму всех целых чисел от a до 400 (значение a вводится с клавиатуры; a ≤ 400);
# sum_of_numbers = 0
# a = int(input('Type "a" value (should be less or equals 400): '))
# for num in range(a, 400 + 1):
#     sum_of_numbers += num
# print("Sum of numbers in the range:", sum_of_numbers)

# 5.28. Найти: а) произведение всех целых чисел от 7 до 14;
# product_of_numbers = 1
# for n in range(7,15):
#     print(n)
#     product_of_numbers *= n
# print(product_of_numbers)

# 5.30. Найти: а) сумму кубов всех целых чисел от 25 до 40;
# sum_of_cube = 0
# for n in range(25,40):
#     cube = n**3
#     sum_of_cube += cube
#     print(cube)
# print(sum_of_cube)

# Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он увеличивал пробег на 10 % от пробега
# предыдущего дня. Определить: а) пробег лыжника за второй, третий, ..., десятый день тренировок;
# first_day = 10
# next_day = first_day
# n = 2
# result = first_day
# while n <= 10:
#     next_day += (next_day * 0.1)  # Increasing the distance by 10% each day
#     result += next_day
#     print(f"Day {n}: {next_day:.2f} km")
#     n += 1

# 5.49. Гражданин 1 марта открыл счет в банке, вложив 1000 usd. Через каждый месяц размер вклада увеличивается
# на 2 % от имеющейся суммы. Определить: а) прирост суммы вклада за первый, второй, ..., десятый месяц;
# б) сумму вклада через три, четыре, ..., двенадцать месяцев.
# zero_month = 1000
# next_month = zero_month
# month = 1
# result = zero_month
# while month <= 10:
#     next_month +=(next_month * 0.2)
#     result += next_month
#     incr_depos = next_month - zero_month
#     print(f'Mont {month}- increase in the amount of the deposit: {incr_depos:.2f} usd; full deposit: {next_month:.2f} usd')
#     month += 1

# # Print all even numbers from 1 to 20 with for
# for n in range(1,21):
#     if n % 2 == 0:
#         print(n)
#
# # with while
# n = 1
# while n <= 20:
#     if n % 2 == 0:
#         print(n)
#     n +=1

# Print the sum of all odd numbers from 1 to 100
# sum = 0
# for i in range(1,100,2):
#     sum = sum + i
# print(sum)
#
# Find the product of all prime numbers from 1 to 50.---
# prod = 1
# for i in range(1,51):
#     prod = prod * i
# print(prod)

# Given a list of integers, find and print all the numbers that are divisible by both 3 and 5.
list = [152, 58, 65, 85, 4, 55, 9, 27, 99, 15]
for i in list:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
