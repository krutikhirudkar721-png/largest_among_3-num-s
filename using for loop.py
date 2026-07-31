#Using for loop Hello Students

n1 = int(input("Enter first number: "));
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

# Put numbers in a list

numbers = [n1, n2, n3]
# Loop to find the largest

largest = n1
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")
