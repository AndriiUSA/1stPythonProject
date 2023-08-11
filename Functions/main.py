# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")
# greet('Andrii')

# def add_numbers(a, b):
#     result = a + b
#     return result
#
# first_sum_result = add_numbers(5, 3)
# second_sum_result = add_numbers(4,2)
# print(first_sum_result, second_sum_result)

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

def addition(a, b):
    result_add = a * b
    return result_add

n1 = float(input('Type number 1: '))
n2 = float(input('Type number 2: '))
addition_add = addition(n1,n2)
print(addition_add)