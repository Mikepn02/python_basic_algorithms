class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Undefined")

# Example usage

calculator = Calculator()

# Addition
print("Enter two values to get the sum: ")
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))
result = calculator.add(x, y)
print("The sum is: ",f"{x} + {y} =", result)

# Subtraction
print("Enter two values to get the difference: ")
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))
result = calculator.subtract(x, y)
print("The difference is: ",f"{x} - {y} =", result)

# Multiplication
print("Enter two values to get the product: ")
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))
result = calculator.multiply(x, y)
print("The product is: ",f"{x} * {y} =", result)

# Division
print("Enter two values to get the quotient: ")
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))
result = calculator.divide(x, y)
print("The quotient is: ",f"{x} / {y} =", result)

# Division by zero (raises an error)
result = calculator.divide(x, y)
print(f"{x} / 0 =", result)