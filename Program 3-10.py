f=int(input("Enter the temperature in fahrenheit:"))
c=(f-32)*(5/9)
print("temperature in celsius:",c)

print("")

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

avg=(a+b)/2

d1=a-avg
d2=b-avg

print("the average of two number:",avg)
print("the deviation of first number:",d1)
print("the deviation of second number:",d2)
print("")

a=int(input("enter the number:"))

if a % 7 ==0:
    print("the number is divisible by 7")
else:
    print("the number is not divisible by 7")

print("")


a=int(input("enter the M.R.P of 1st item:"))
b=int(input("enter the quantity of 1st item:"))
c=int(input("enter the M.R.P of 2nd item:"))
d=int(input("enter the quantity of 2nd item:"))
e=int(input("enter the M.R.P of 3rd item:"))
f=int(input("enter the quantity of 3rd item:"))
d1=int(input("enter the discount in percent:"))
tx=int(input("enter the tax in percent"))

x=a*b
y=c*d
z=e*f

disa=x*(d1/100)
sp1=x-disa
tx1=sp1*(tx/100)
f1=sp1+tx1

disb=y*(d1/100)
sp2=y-disb
tx2=sp2*(tx/100)
f2=sp2+tx2

disc=z*(d1/100)
sp3=z-disc
tx3=sp3*(tx/100)
f3=sp3+tx3

bill=f1+f2+f3

print("the final bill amount:",bill)
print("")

a=int(input("enter the score in 1st exam out of 100:"))
b=int(input("enter the score in 2nd exam out of 100:"))
c=int(input("enter the score of sports event out of 100:"))
d=int(input("enter the score of 1st activity out of 100:"))
e=int(input("enter the score of 2nd activity out of 100:"))
f=int(input("enter the score of 3rd activity out of 100:"))

ex=(a+b)/2
act=(d+e+f)/3

w1=ex*0.5
w2=c*0.2
w3=act*0.3

result=w1+w2+w3

print("final result in:",result)

print("\n")

a=int(input("enter the number of 5 ruppees coins/note in piggy bank:"))
b=int(input("enter the number of 10 ruppees coins/note in piggy bank:"))
c=int(input("enter the number of 50 ruppees note in piggy bank:"))

total=(a*5)+(b*10)+(c*50)

print("the total amount in piggy bank:",total)

print("\n")


a=int(input("enter the basic pay:"))

hra=a+(a*0.15)
ta=a+(a*0.07)
salary=a+hra+ta

print("the final salary of employee:",salary)

print("\n ")

m=float(input("enter the mass of object in kg :"))
c=float(input("enter the velocity in meter per second :"))

e=m*c*c

print("momentum:",e)

print("\n ")
