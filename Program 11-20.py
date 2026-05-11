#Question-11
a= int(input("Enter your age: "))
if (a>=18) :
    print("You are eligible to vote")

elif a<18:
    b=18-a
    print("You are not eligible to vote")
    print(b,"years are left to be eligible ")

print("NAITIK SINGHAL")



#Question-12
a=input("Enter any character: ")

if a.isalpha() :
    print("Character given by the user is an alphabet")
 
elif a.isdigit() :
    print("Character given by the user is an digit")
    
elif a.isspace() :
    print("Character given by the user is an space ")
print("NAITIK SINGHAL")


#Question-13
a= input("Enter any character: ")

if a.islower() :
    a=a.upper()
    print(a)
elif a.isupper():
    a=a.lower()
    print(a)
print("NAITIK SINGHAL")


#Question-14    
salary= int(input("Enter your salary: "))
gender= input("Enter your gender Male as M and Female as F: ")

if gender=="M":
  if (salary <10000) :
       bonus= salary*0.07
       total = salary + bonus
       print(bonus)
       print("Total salary ",total)
  else:
       bonus= salary*0.05
       total=salary + bonus
       print(bonus)
       print("Total salary",total)

elif gender=="F":
   if (salary <10000) :
       bonus= salary*0.12
       total = salary + bonus
       print(bonus)
       print("Total salary ",total)
   else:
       bonus= salary*0.1
       total=salary + bonus
       print(bonus)
       print("Total salary",total)
print("NAITIK SINGHAL")



#Question-15
a=int(input("Enter the marks of subject 1: "))
b=int(input("Enter the marks of subject 2: "))
c=int(input("Enter the marks of subject 3: "))
d=int(input("Enter the marks of subject 4: "))

total=a+b+c+d
aggregate=total/4

print("Total marks: ",total)
print("Aggregate: ",aggregate,"%")

if aggregate>75:
    print("Grade: Distinction")
elif aggregate>=60 and aggregate<75:
    print("Grade: First Division")
elif aggregate>=50 and aggregate<60:
    print("Grade: Second Division")
elif aggregate>=40 and aggregate<50:
    print("Grade: Third Division")
else:
    print("Grade: Fail")

print("NAITIK SINGHAL")


#Question-16
import math

a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

d=b**2 - 4*a*c

if d>0:
    root1=(-b + math.sqrt(d))/(2*a)
    root2=(-b - math.sqrt(d))/(2*a)
    print("Roots are real and different")
    print("Root1:",root1)
    print("Root2:",root2)

elif d==0:
    root=-b/(2*a)
    print("Roots are real and same")
    print("Root:",root)

else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-d)/(2*a)
    print("Roots are complex")
    print("Root1: ",real_part,"+",imaginary_part,"-i")
    print("Root2: ",real_part,"-",imaginary_part,"-i")

print("NAITIK SINGHAL")


#Question-17
# 1) First 10 natural numbers
i = 1
count = 0
sum1 = 0

while count < 10:
    sum1 += i
    i += 1
    count += 1

avg1 = sum1 / 10
print("First 10 numbers sum:", sum1)
print("First 10 numbers average:", avg1)


# 2) First 10 odd numbers
i = 1
count = 0
sum2 = 0

while count < 10:
    sum2 += i
    i += 2
    count += 1

avg2 = sum2 / 10
print("\nFirst 10 odd numbers sum:", sum2)
print("First 10 odd numbers average:", avg2)


# 3) First 10 even numbers
i = 2
count = 0
sum3 = 0

while count < 10:
    sum3 += i
    i += 2
    count += 1

avg3 = sum3 / 10
print("\nFirst 10 even numbers sum:", sum3)
print("First 10 even numbers average:", avg3)

print("NAITIK SINGHAL")

#Question-18
positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    if num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1
    num = int(input("Enter a number (-1 to stop): "))    
    
#Calculating averages
if positive_count != 0:
    positive_avg = positive_sum / positive_count
else:
    positive_avg = 0

if negative_count != 0:
    negative_avg = negative_sum / negative_count
else:
    negative_avg = 0

print("\nAverage of positive numbers:", positive_avg)
print("Average of negative numbers:", negative_avg)
print("NAITIK SINGHAL")

#Question-19
a=int(input("Enter a number: "))
sum=0
while a>0:
    digit=a%10
    sum += digit
    a=a//10
print("Sum of its digits= ",sum)
print("NAITIK SINGHAL")


#Question-20
  
num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
print("NAITIK SINGHAL")


        


    

 
