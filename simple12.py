import sys

def add_num(a, b): # function for addition
    sum = a + b
    return sum # return value

num1 = int(sys.argv[1]) # first argument is num1
num2 = int(sys.argv[2]) # second argument is num2

print("The sum is", add_num(num1, num2)) # call the function and print the result

