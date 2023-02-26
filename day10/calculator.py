from art import logo
print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


# input
def calculator():
    continue_calc = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()


calculator()
