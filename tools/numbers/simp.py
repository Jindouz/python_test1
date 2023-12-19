from icecream import ic



# Adding two numbers together
def add(a, b):
    print("==Adding two numbers==")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result: ", a + b)
    return a + b

# Subtracting two numbers
def subtract(a, b):
    print("==Subtracting two numbers==")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a - b)
    return a - b
