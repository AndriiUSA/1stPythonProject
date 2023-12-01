# Add
def add(n1, n2):
    return n1 + n2
# Substructure
def sub(n1,n2):
    return n1 - n2
# Multiply
def mult(n1, n2):
    return n1 * n2
# Divide
def dev(n1, n2):
    return n1 / n2
# Dictionary with operstions
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": dev
}
num1 = int(input("What's is first number?"))
for symbol in operations:
    print(symbol)
operations_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's is second number?"))
calculation_function = operations[operations_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {first_answer}")

operations_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?"))
calculation_function = operations[operations_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")