#Question-41

#for i in range (1,7):

# ch= 'A'

# print()

# for j in range (1, i+1):

#   print (ch, end='')
#   ch=chr(ord (ch)+ 1)
#print("\nNAITIK SINGHAL")


#Question-42

#while (1):

#  name=input ("Enter your name:")

#  if name.isalpha== False:
#      print("Invalid Name, sorry you cannot proceed.")
    
#      break

#  else:

#      pan_card_no=input ("Enter your Pan card number: ")

#      if pan_card_no.isalnum( )== False:

#        print ("Invalid Pan Card Number, sorry you connot peroceed.")

#        break

#      print ("Please check", name)

#      print("please check your Pan Card member is: ",pan_card_no)

#      break 
#print("\nNAITIK SINGHAL")


#Question-43

#message = "HelloWorld"
#index=0

#while index < len(message):

#  letter = message[index]

#  print(chr(ord (letter) + 3), end = ' ')

#  index += 1
#print("\nNAITIK SINGHAL")



#Question-44

#letter='''Dear students,

#I am fleesed to inform you that,

#there is a workshop on python in college tomorrow, Everyone should come and

#there will be a quiz in bo a quiz in hithers, whoecover инте will win a Gold Medal.'''

#print(letter.split('\n'))
#print("\nNAITIK SINGHAL")


#Question-45

#str1= 'ABCDEFGH'

#str2 = "ate"

#for letters in str1:

# print((letters + str2),end=' ')
#print("\nNAITIK SINGHAL")


#Question-46

#def remove_vowels(s):

#    new_str=" "

#    for i in s:
#        if i not in "aeiouAΕΙΟU":
#           new_str += i
#    print("The string without vowel is: ", new_str)
#str=input("enter a string:")
##remove_vowels(str)
#print("\nNAITIK SINGHAL")


#Question-47

#def find_chr(S,c):
 #   index = 0
  #  while (index<len(S)):
   #     if S[index]==c:
    #        print(c, "found in string at index:", index)
     #       return
      #  index+=1
#    print(c,"is not present in the string")
#str=input("enter a string:")
#chr=input("enter a character to be searched:")
#find_chr(str,chr)

#print("NAITIK SINGHAL")


#Question-48

#def add_2(x):

# x+=2

 #return x

#num_list = [1,2,3,4,5,6,7]
#print("Original List is: ", num_list)
#new_list=list(map(add_2, num_list))
#print("New List is:",new_list)
#print("NAITIK SINGHAL")


#Question-49

#def add (x, y):
# return x+y
#list1=[1,2,3,4,5]
#list2= [6,7,8,9,10]
#list3= list (map(add, list1, list2))

#print ("Sum of of",list1, "and", list2 ,"=", list3)
#print("NAITIK SINGHAL")


#Question-50


#import functools
#def add (x,y):
#    return x+y
#num_list=[1,2,3,4,5]
#print("sum of values in list=")
#print(functools.reduce(add,num_list))

#print("NAITIK SINGHAL")


#Question-51

#def to_lower(str):
#    return str.lower()

#list1 =[ "HELLO", "WELLCOME", "TO", "PYTHON"]

#list2=list(map (to_lower,list1))

#print("list in lowercase character is", list2)

#print("NAITIK SINGHAL")


#Question-52

def squares(x):

 return x*x

sq_list=list(map (squares, range(1, 11)))

print ("list of square from 1-10:",sq_list)
print("NAITIK SINGHAL") 


        
