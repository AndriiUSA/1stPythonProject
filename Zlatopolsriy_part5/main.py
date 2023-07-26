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
sum_of_cube = 0
for n in range(25,40):
    cube = n**3
    sum_of_cube += cube
    print(cube)
print(sum_of_cube)