# # 1.1 Вывести на одной строке числа 31, 18 и 79 с одним пробелом между ними. Текст '31 18 79' не использовать.
# my_list = [31, 18, 79]
# print(my_list[0], my_list[1], my_list[2])
#
# # 1.2 Вывести на одной строке числа 47, 52 и 150 с двумя пробелами между ними. Текст '47 52 150' не использовать.
# new_list = [47, 52, 150]
# space = ' '
# print(new_list[0], space, new_list[1], space, new_list[2])
#
# # 1.3 Вывести на экран числа 50 и 10 одно под другим.
# under_list = [50, 10]
# for under in under_list:
#     print(under)
#
# # 1.4. Вывести на экран числа 5, 10 и 21 одно под другим.
# print('\r')
# under_new_list = [5, 10, 21]
# for under in under_new_list:
#     print(under)
#
# # 1.5. Получить на экране следующее:
# # 1
# # 2
# print('\r')
# number_on_screen = [1, 2]
# for number in number_on_screen:
#     print(number)
#
# # 1.6. Число π примерно равно 3,1415926. Вывести на экран это
# # число с тремя цифрами в дробной части. Текст '3.142' не использовать.
# p = 3.1415926
# print(round(p,3))
#
# # 1.7. Число e (основание натурального логарифма) приблизи-
# # тельно равно 2,71828. Вывести на экран это число с точностью до десятых. Текст '2.7' не использовать.
# e = 2.71828
# print(round(e,1))

# 1.8. Составить программу вывода на экран числа, вводимого
# с клавиатуры. Выводимому числу должно предшествовать со общение «Вы ввели число».
# number = input('Type your number: ')
# print('You typed number: ' + number)

# Составить программу вывода на экран числа, вводимого с клавиатуры.
# После выводимого числа должно следовать сообщение «– вот какое число Вы ввели».
# number = input('Type your number: ')
# print( number + ' - you typed.')

# Составить программу, которая запрашивает имя человека и повторяет его на экране.
# name = input('Type your name: ')
# print(name)

# 1.11. Составить программу, которая запрашивает название
# # футбольной команды и повторяет его на экране со словами «– это чемпион!».
# sport_teame = input('what is your favorite Sport Team?: ')
# print(sport_teame + '- is Champion')

# 1.12. Напишите программу, в которую вводится имя человека и выводится на экран
# приветствие в виде слова «Привет», после которого должна стоять запятая, введенное имя
# и восклицательный знак. После запятой должен стоять пробел, а перед восклицательным знаком пробела быть не должно.
# name = input('What is your name: ')
# print('Hi, ' + name + '!')

# 1.13. Напишите программу, в которую вводится целое число, после чего на экран выводится следующее
# и предыдущее целое число.
number = int(input('Type number: '))
next_number = number + 1
previous_number = number - 1
print(f'Next number after {number} is {next_number}')
print(f'Previous  number before {number} is {previous_number}')