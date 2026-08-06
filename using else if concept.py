# Largest-among-3-numbers
# *this is the program to find largest among three numbers in Python
#1.using if else concept
    n1=int(input("Enter first number: "))
    n2=int(input("Enter second number: "))
    n3=int(input("Enter third number: "))
    if n1>n2 and n1>n3:
      print(f"The largest number is: {n1}")
    elif n2>n1 and n2>n3:
      print(f"The largest number is: {n2}")
    else:
      print(f"The largest number is: {n3}")s
