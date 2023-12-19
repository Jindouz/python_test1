from icecream import ic


# Calculates the sum of digits
def sumofdigits(number):
    print("==Sum of Digits==")
    number = int(input("Enter a number: "))
    sum_res = sum(int(digit) for digit in str(number))
    print("The sum is: ",sum_res)
    return sum_res

# Checks if the number is palindrome
def ispal(number):
    print("==Palindrome Check==")
    number = int(input("Enter a number: "))
    num_str = str(number)
    ispal_res = num_str == num_str[::-1]
    print("Result: ",ispal_res)
    return ispal_res
