#Question-31
# Program to convert time in hours and minutes to total minutes

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

total_minutes = (hours * 60) + minutes

print("Time in minutes =", total_minutes)
print("NAITIK SINGHAL")

#Question-32
def volume(length=1, breadth=1, height=1):
    return length * breadth * height

# Calling function with default values
print("Volume with default values:", volume())

# Calling function with user-defined values
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Volume of cuboid:", volume(l, b, h))
print("NAITIK SINGHAL")

#Question-33
 
def factorial(n):
    if n == 0 or n == 1:   # Base condition
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

# Taking input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
print("NAITIK SINGHAL")


#Question-34
def gcd(a, b):
    if b == 0:          # Base condition
        return a
    else:
        return gcd(b, a % b)   # Recursive call

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD of", num1, "and", num2, "is", gcd(num1, num2))


print("NAITIK SINGHAL")


#Question-35
def power(x, y):
    if y == 0:          # Base condition
        return 1
    else:
        return x * power(x, y - 1)   # Recursive call

# Taking input from user
x = int(input("Enter base (x): "))
y = int(input("Enter exponent (y): "))

if y < 0:
    print("This program does not handle negative exponents.")
else:
    print(x, "raised to", y, "is", power(x, y))

print("NAITIK SINGHAL")


#Question-36
def fibonacci(n):
    if n == 0:          # Base case
        return 0
    elif n == 1:        # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)   # Recursive call

# Taking input from user
terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

print("NAITIK SINGHAL")


#Question-37

# Taking list input from user
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

# Assume first element is largest
largest = numbers[0]

# Comparing each element
for i in numbers:
    if i > largest:
        largest = i

print("Largest number in the list is:", largest)


print("\nNAITIK SINGHAL")



#Question-38

# Creating a list
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print("Original List:", lst)

# Insert operation
pos = int(input("Enter position to insert (starting from 0): "))
value = int(input("Enter value to insert: "))

lst.insert(pos, value)
print("List after insertion:", lst)

# Delete operation
del_pos = int(input("Enter position to delete (starting from 0): "))

if 0 <= del_pos < len(lst):
    lst.pop(del_pos)
    print("List after deletion:", lst)
else:
    print("Invalid position for deletion.")


print("NAITIK SINGHAL")


#Question-39

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)

print("NAITIK SINGHAL")



#Question-40

# Function to check positive numbers
def is_positive(num):
    return num > 0

# Taking input
lst = list(map(int, input("Enter elements separated by space: ").split()))

# Using filter function
positive_list = list(filter(is_positive, lst))

print("Original List:", lst)
print("List with only positive numbers:", positive_list)

print("NAITIK SINGHAL")
