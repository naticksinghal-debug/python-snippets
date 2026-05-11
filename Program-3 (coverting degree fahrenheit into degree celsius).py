unit= input("Is this temprature in Celcius or Fahrenheit (C/F): ")
temp= float(input("Enter the temprature; "))

# (C * 9/5) + 32 = F
if unit == "C":
    temp= round((9*temp) /5 + 32, 1)
    print(f"The temprature in Fahrenheit is: {temp}")





#convert degrees fahrenheit into degree celsius.


temp= float(input("Enter the temprature in degree Fahrenheit: "))



# (F-32) * 5/9 = C          
temp= round((F-32)*(5/9), 1)
print(f"The temprature in degree Celsius is: {temp}")

    

