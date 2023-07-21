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
# Известны координаты левого нижнего и правого нижнего углов каждого из них. Найти координаты левого нижнего и
# правого верхнего углов минимального прямоугольника, содержащего указанные прямоугольники.
# a_x = int(input('Type Ax(first square): '))
# a_y = int(input('Type Ay(first square): '))
# b_x = int(input(f'Type Bx(first square) (more then {a_x}): '))
# print(f'By:{a_y}')
# y_side_1 = int(input('Type AD side (first square) light parallel Y axis: '))
# d_y = a_y + y_side_1
# e_x = int(input('Type Ex(second square): '))
# e_y = int(input('Type Ey(second square): '))
# f_x = int(input(f'Type Fx(second square) (more then {e_x}): '))
# print(f'Fy:{e_y}')
# y_side_2 = int(input('Type EH side (second square) light parallel Y axis: '))
# h_y = e_y + y_side_2
# if y_side_1 < y_side_2:
#     print(f'(First square coordinates Ax:{a_x};Ay:{a_y}. Bx:{b_x};By{a_y}. Cx:{b_x};Cy:{y_side_1}. Dx:{a_x},Dy{y_side_1}.')
# else:
#     print(f'(Second square coordinates Ex:{e_x};Ey:{e_y}. Fx:{f_x};Fy{e_y}. Gx:{f_x};Gy:{y_side_2}. Hx:{e_x},Hy{y_side_2}.')

# 4.25. Дано целое число n. Вывести на экран следующее за ним четное число.
# n = int(input('Type integer n: '))
# if n % 2 > 0:
#     m = n + 1
#     print(m)
# else:
#     m = n + 2
#     print(m)

# 4.25. Дано двузначное число. Определить какая из его цифр больше:
# number = input('Type two characters number: ')
# a = int(number[0])
# b = int(number[1])
# if a == b:
#     print('Characters same')
# elif a > b:
#     print('First character greater')
# else:
#     print('Second character greater')