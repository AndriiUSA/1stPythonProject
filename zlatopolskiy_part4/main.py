# 4.11. Известны две скорости: одна выражена в километрах в час, другая – в метрах в секунду.
# Какая из скоростей больше?
# speed_km = float(input('Type speed in km/h: '))
# speed_m = float(input('Type speed in m/s: '))
# speed_km_to_m = speed_km * 1000/3600
# if speed_km_to_m > speed_m:
#     print(f'speed in km/h {round(speed_km_to_m, 2)} faster then speed in m/s {speed_m}')
# else:
#     print(f'Speed in m/s {speed_m} faster then speed in km/h {round(speed_km_to_m,2)}')

# 4.17. Известны год и номер месяца рождения человека, а также год и номер месяца сегодняшнего дня
# (январь – 1 и т. д.). Определить возраст человека (число полных лет). В случае совпадения
# # указанных номеров месяцев считать, что прошел полный год.
# year = int(input('Type your birthday year: '))
# month = int(input('Type your birthday month: '))
# today_year = 2023
# today_month = 7
# years_old = today_year - year
# month_old = today_month - month
# if month_old < 0:
#     years_before = years_old - 1
#     month_before = 12 - (month - today_month)
#     print(f'Your age is {years_before}years, {month_before}month.')
# else:
#     print(f'Your age is {years_old}yars, {month_old}month.')

# 4.18. Известны площади круга и квадрата. Определить: а) уместится ли круг в квадрате?
# б) уместится ли квадрат в круге?
# circle_area = float(input('Type circle area A: '))
# square_area = float(input('Type square area B: '))
# p = 3.1416926
# circle_diametr = 2 * (circle_area / p)**0.5
# triangle_hypotenuse = (2 * square_area)**0.5
# square_side = square_area ** 0.5
# if triangle_hypotenuse < circle_diametr:
#     print('A square fits into a circle')
# elif circle_diametr < square_side:
#     print('The circle is placed in a square')
# else:
#     print('Nothing fit nothing')

# 4.20*. Даны два прямоугольника, стороны которых параллельны или перпендикулярны осям координат.
# Известны координаты левого нижнего и правого ерхнего углов каждого из них. Найти координаты левого нижнего и
# правого верхнего углов минимального прямоугольника, содержащего указанные прямоугольники.
first_left_bottom_X = int(input('Type first left bottom square X coordinate: '))
first_left_bottom_Y = int(input('Type first left bottom square Y coordinate: '))
first_right_top_X = int(input(f'Type first right top square X coordinate more then {first_left_bottom_X}: '))
first_right_top_Y = int(input(f'Type first right top square Y coordinate more then {first_left_bottom_Y}: '))

second_left_bottom_X = int(input('Type second left bottom square X coordinate: '))
second_left_bottom_Y = int(input('Type second left bottom square Y coordinate: '))
second_right_top_X = int(input(f'Type second right top square X coordinate more then {second_left_bottom_X}: '))
second_right_top_Y = int(input(f'Type second right top square Y coordinate coordinate more then {second_left_bottom_Y}: '))

# Left smallest X and Y coordinate
if first_left_bottom_X < second_left_bottom_X:
    print(f'Min Left bottom X Coordinate: {first_left_bottom_X}')
else:
    print(f'Min Left bottom X Coordinate: {second_left_bottom_X}')
if first_left_bottom_Y < second_left_bottom_Y:
    print(f'Min Left bottom Y Coordinate: {first_left_bottom_Y}')
else:
    print(f'Min Left bottom Y Coordinate: {second_left_bottom_Y}')

# Right smallest X and Y coordinate
if first_right_top_X < second_right_top_X:
    print(f'Min Right top X Coordinate: {first_right_top_X}')
else:
    print(f'Min Right top X Coordinate: {second_right_top_X}')
if first_right_top_Y < second_right_top_Y:
    print(f'Min Right top Y Coordinate: {first_right_top_Y}')
else:
    print(f'Min Right top X Coordinate: {second_right_top_Y}')

# 4.25. Дано целое число n. Вывести на экран следующее за ним четное число.
# n = int(input('Type integer n: '))
# if n % 2 > 0:
#     m = n + 1
#     print(m)
# else:
#     m = n + 2
#     print(m)

# # 4.25. Дано двузначное число. Определить какая из его цифр больше:
# number = input('Type two characters number: ')
# a = int(number[0])
# b = int(number[1])
# if a == b:
#     print('Characters same')
# elif a > b:
#     print('First character greater')
# else:
#     print('Second character greater')