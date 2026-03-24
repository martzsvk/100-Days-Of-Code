import art

# Functions for mathematical operations
def add(first_n,second_n):
    return first_n + second_n

def subtract(first_n,second_n):
    return first_n - second_n

def multiply(first_n,second_n):
    return first_n * second_n

def divide(first_n,second_n):
    return first_n / second_n

# Main function of calculator
def calculator():
    print(art.logo)
    first_n = float(input("What's the first number? "))
    continuation = True
    while continuation:
        operation = input("+\n"
                          "-\n"
                          "*\n"
                          "/\n"
                          "What operation do you want to execute? ")
        second_n = float(input("What's the second number? "))

        if operation == "+":
            result = add(first_n,second_n)
            print(f"{first_n} + {second_n} = {result}")
        elif operation == "-":
            result = subtract(first_n,second_n)
            print(f"{first_n} - {second_n} = {result}")
        elif operation == "*":
            result = multiply(first_n,second_n)
            print(f"{first_n} * {second_n} = {result}")
        elif operation == "/":
            result = divide(first_n,second_n)
            print(f"{first_n} / {second_n} = {result}")

        continuation = input(f"Type 'y' if you want to continue calculating with {result} or type 'n' if you want to start a new calculation: ")
        if continuation == "y":
            first_n = result
        else:
            continuation = False
            print("\n" * 20)
            calculator()



calculator()







