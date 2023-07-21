# вычисления значения функции y = 17x2 – 6x + 13 при любом значении x
# x = int(input('For formula y= 17x(sqr) - 6x + 13 input X: '))
# y = 17*x**2 - 6*x + 13
# print(y)

# вычисления значения функции y = 3a2 + 5a – 21 при любом значении а.
# a = int(input('For formula y = 3a(sqr) + 5a -21 input a: '))
# y = 3*a**2 + 5*a - 21
# print(y)

# 2.2 Составить программу вычисления значения функции при любом значении а.
# a = int(input('Type a value: '))
# y = (a**2 + 10) / (a**2 + 1)**0.5
# print(y)

# 2.3. Составить программу:
# a)
# import math
# a = int(input('Type a value: '))
# x = ((2*a + math.sin(abs(3*a)))/3.56)**0.5
# print(x)
# b)
# import math
# x = int(input('Type a value: '))
# y = math.sin((3.2 + (1 + x )**0.5) / abs(5 * x))
# print(y)

# # 2.4. Дана сторона квадрата. Найти его периметр.
# square_side = int(input('Type sqiare side: '))
# square_perimetr = square_side * 4
# print(square_perimetr)

# # 2.5. Дан радиус окружности. Найти ее диаметр.
# radius = int(input('Type radius: '))
# dimetr = radius * 2
# print(dimetr)

# 2.6. Считая, что Земля – идеальная сфера с радиусом R ≈ 6350 км, определить расстояние до линии
# # горизонта от точки с заданной высотой над Землей.
# earth_radius = 6350
# elevation = int(input('Type your elevation under earth: '))
# horizon = int(((earth_radius + elevation)**2 - earth_radius**2)**0.5)
# print(f'Horizon: {horizon} km')

# # 2.7. Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.
# cube_edge = int(input('Type cube edge: '))
# cube_volume = cube_edge** 3
# cube_area = cube_edge ** 2 * 6
# print(f'Cube volume: {cube_volume}')
# print(f'Cube area: {cube_area}')

# 2.8. Дан радиус окружности. Найти длину окружности и площадь круга.
# radius = int(input('Type radius: '))
# circle_circumference = 2 * 3.14 * radius
# circle_area = 3.141592653 * radius**2
# print(f'Circle circumference: {circle_circumference}')
# print(f'Circle area {circle_area}')

# 2.9. Составить программу:
# а) вычисления значения функции z = 2x3 – 3,44xy + 2,3x2 – 7,1y + 2 при любых значениях х и y;
# x = int(input('Type X: '))
# y = int(input('Type Y: '))
# z = 2 * x**3 - 3.44 * x * y + 2.3 * x**2 - 7.1 * y + 2
# print(f'Z = {z}')
# a = int(input('Type A: '))
# b = int(input('Type B: '))
# x = 3.14 * (a + b)**3 + 2.75 * b**2 - 12.7 * a - 4.1
# print(f'X = {x}')

# 2.10. Даны два целых числа. Найти: а) их среднее арифметическое; # б) их среднее геометрическое.
# x = int(input('Type first number: '))
# y = int(input('Type second number: '))
# number_average = (x + y) / 2
# number_geometric_mean = (x * y)**0.5
# print(f'Average {number_average}')
# print(f'Geometric mean: {number_geometric_mean}')

# 2.11 Известны объем и масса тела. Определить плотность материала этого тела.
# density = int(input('Type density: '))
# weight = int(input('Type weight: '))
# volume = density * weight
# print(f'Volume: {volume}')

# 2.12. Известны количество жителей в государстве и площадь его территории. Определить плотность
#  населения в этом государстве.
# square = int(input('Type square of land: '))
# population = int(input('Type population: '))
# population_density = population / square
# print(population_density)

# 2.13. Составить программу решения линейного уравнения ax + b = 0 (a ≠ 0).
# a = int(input('Type A: '))
# b = int(input('Type B: '))
# x = - b/a
# print(f'X = {x}')

# 2.14. Даны катеты прямоугольного треугольника. Найти его гипотенузу.
# ac = int(input('Type AC leg value: '))
# cb = int(input('Type CB leg value: '))
# ab = (ac**2 + cb**2)**0.5
# print(f'Hypotenuse AB is: {ab}')

# 2.15. Найти площадь кольца по заданным внешнему и внутреннему радиусам.
# in_radius = int(input('Type inside radius: '))
# out_radius = int(input('Type outside radius: '))
# ring_area = 3.141592653 * out_radius**2 - 3.141592653 * in_radius**2
# print(f'Ring area: {ring_area}')

# # 2.16. Даны катеты прямоугольного треугольника. Найти его периметр.
# ac = int(input('Type AC leg value: '))
# cb = int(input('Type CB leg value: '))
# perimeter = round((ac**2 + cb**2)**0.5 + ac + cb, 2)
# print(f'Triangle perimeter is: {perimeter}')

