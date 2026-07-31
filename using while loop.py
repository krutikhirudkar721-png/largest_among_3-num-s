# Using while loop print Hello Students

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
numbers = [n1, n2., n3]

# Variables for while loop

largest = n1
index = 0

# Loop running until index reaches length of list (3)
while index < len(numbers):
    if numbers[index] > largest:
        largest = numbers[index]
    index += 1  # Move to next number

print(f"The largest number is: {largest}")
