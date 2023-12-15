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

def calculator():
    num1 = float(input("What's is first number?"))
    for symbol in operations:
        print(symbol)
    should_continiue = True

    while should_continiue:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's is next number?"))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        cycle = input(f"Type 'y' to continue to calculation with {answer}, or type 'c' to new calc, or press anything else to exit.: ")
        if cycle == "y":
            num1 = answer
        elif cycle == "c":
            should_continiue = False
            calculator()
        else:
            should_continiue = False
calculator()