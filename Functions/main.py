def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
greet('Andrii')

def add_numbers(a, b):
    result = a + b
    return result

first_sum_result = add_numbers(5, 3)
second_sum_result = add_numbers(4,2)
print(first_sum_result, second_sum_result)

# def greet(name="User"):
#     print(f"Hello, {name}!")
#
# greet()        # Output: Hello, User!
# greet("John")  # Output: Hello, John!
#

# def square(num):
#     """
#     Returns the square of a number.
#
#     Args:
#     num (int): The input number.
#
#     Returns:
#     int: The square of the input number.
#     """
#     return num ** 2
# MY:
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mult(a,b):
#     return a * b
# def div(a,b):
#     return a / b
# # Opewration
# n1 = float(input('Number 1: '))
# operation = input('+,-,*,/ ')
# n2 = float(input('Number 2: '))
# # mathe
# if operation == "+":
#     res = add(n1, n2)
# elif operation == "-":
#     res = sub(n1, n2)
# elif operation == "*":
#     res = mult(n1, n2)
# elif operation == "/":
#     if n2 == 0:
#         print("Cannot divide by zero")
#         res = None
#     else:
#         res = div(n1, n2)
# else:
#     print('Somthing wrong!')
#     res = None
# if res is not None:
#     print(f'Result: {res}')
#Chat GPT:
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b if b != 0 else None
# Operation
n1 = float(input('Number 1: '))
operation = input('+, -, *, /: ')
n2 = float(input('Number 2: '))
# Dictionary to map operations to functions
operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}
# Math
if operation in operations:
    res = operations[operation](n1, n2)
    if res is not None:
        print(f'Result: {res}')
    else:
        print("Cannot perform the operation.")
else:
    print('Something wrong!')
