def factorial (n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
result = factorial (number)
print(f"The factorial of {number} is {result}")


def multiply_numbers(a, b):
    result = a * b
    return result

# Example usage
num1 = 5
num2 = 7
result = multiply_numbers(num1, num2)
print(f"The result of multiplying {num1} and {num2} is {result}")

def divide_numbers(a, b):
    # Check if the denominator (b) is not zero to avoid division by zero error
    if b != 0:
        quotient = a / b
        return quotient
    else:
        print("Error: Division by zero is not allowed.")
        return None

# Example usage
number1 = 10
number2 = 2
result = divide_numbers(number1, number2)

if result is not None:
    print(f"The quotient of dividing {number1} by {number2} is {result}")

