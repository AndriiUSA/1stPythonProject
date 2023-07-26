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

# 5.9. Напечатать таблицу перевода расстояний в дюймах в сантиметры для значений 10, 11, ..., 22 дюйма (1 дюйм = 25,4 мм).
# for inch in range(10,23):
#     cm = inch * 2.54
#     print(f'{inch} inches = {cm} centimeters')

# 5.10 Напечатать таблицу перевода 1, 2, ... 20 долларов США в грн по текущему курсу (значение курсас клавиатуры).
exch = float(input('Type exchange rate uah to usd: '))
for usd in range(21):
    uah = usd * exch
    print(f'{usd} us dollars = {uah} ukrainian hryvnia')