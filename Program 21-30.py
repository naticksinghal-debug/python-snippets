# Question-21

n = int(input("Enter the value of n: "))

sum = 0
i = 1

while i <= n:
    sum = sum + (1 / i)
    i += 1

print("Sum of the series =", sum)
print("NAITIK SINGHAL")


# Question-22

n = float(input("Enter the value of n: "))

sum = 0
i = 1

while i <= n:
    sum = sum + (1 / (i*i))
    i += 1

print("Sum of the series =", sum)
print("NAITIK SINGHAL")


# Question-23

sum=0
i=34

while i<=78:
        sum= sum + (i*i)
        i +=2
print("Sum of squares of even numbers from 33 to 78 =", sum)
print("NAITIK SINGHAL")


# Question-24

import math

while True:
    n = int(input("Enter a number: "))

    if n < 0 or n > 999:
        print("Number out of range")
        continue

    print("Square root =", math.sqrt(n))
    break

print("NAITIK SINGHAL")


#Question-25

a=[10,20,30]
i=0

while i < len(a):
    a[i]=a[i]+5
    i +=1

print("Updated list:",a)
print("NAITIK SINGHAL")

#Question-26

a=[]
for i in range(1,51):
    if i%3==0 or i%6==0:
     a.append(i)


print (a)
print("NAITIK SINGHAL")

#Question-27

list1= ["good", "smart", "fast"]
list2= ["boy", "girl", "car"]

combined_list = []

for i in list1:
    for j in list2:
        combined_list.append(i+" " +j)

print(combined_list)        
print("NAITIK SINGHAL")


#Question-28

import random

# Create a list of 10 random integers
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

# Create odd and even lists
odd_list = []
even_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

# Display the results
print("Random List:", numbers)
print("Even List:", even_list)
print("Odd List:", odd_list)

print("NAITIK SINGHAL")


#Question-29
a=[10,20,30,40,50]
total =sum(a)
mean=total/len(a)
print("Sum= ",total)
print("Mean=",mean)
print("NAITIK SINGHAL")


#Question-30
n=int(input("Enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("Factorial=",factorial)    

print("NAITIK SINGHAL")






