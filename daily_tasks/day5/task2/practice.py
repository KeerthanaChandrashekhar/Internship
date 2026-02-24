import math_operations

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = math_operations.power(base, exp)
print("The result of", base, "raised to the power of", exp, "is:", result)

user_input = input("Enter a number to find its average: ")
user_input = user_input.split()
numbers = []

for num in user_input:
    numbers.append(float(num))
    
#numbers = list(map(float, user_input.split()))

    

average_result = math_operations.average(numbers)
print("The average of the given numbers is:", average_result)