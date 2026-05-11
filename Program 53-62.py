 #Question-53

s = input("Enter a string: ")
ch = input("Enter a character to search: ")

found = False
for i in range(len(s)):
    if s[i] == ch:
        print("Character found at index:", i)
        found = True
        break

if not found:
    print("Character not present in the string")

#print("NAITIK SINGHAL")
print("")

#Question-54


string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in string:
    if ch not in vowels:
        result += ch

print("String after removing vowels:", result)
print("")
#print("NAITIK SINGHAL")

#Question-55


string = input("Enter a string: ")
char = input("Enter the character to count: ")
count = 0

for ch in string:
    if ch == char:
        count += 1

print("Number of occurrences:", count)
#print("NAITIK SINGHAL")
print("")
#Question-56


t = (5, -3, 8, -1, 10, -7, 4)
positive_tuple = ()

for num in t:
    if num > 0:
        positive_tuple = positive_tuple + (num,)

print("Original Tuple:", t)
print("Tuple with only positive numbers:", positive_tuple)

#print("NAITIK SINGHAL")
print("")

#Question-57


questions = ["What is your name?", "What is your age?", "Where do you live?"]
answers = ["Naitik", "18", "India"]


qa_pairs = list(zip(questions, answers))
print("Question-Answer pairs:")
for pair in qa_pairs:
   print(pair)

#print("NAITIK SINGHAL")
print("")   

#Question-58

# English → Hindi
eng_hindi = {
    "water": "paani",
    "food": "khana",
    "house": "ghar",
    "book": "kitaab",
    "sun": "suraj"
}

# Hindi → French dictionary
hindi_french = {
    "paani": "eau",
    "khana": "nourriture",
    "ghar": "maison",
    "kitaab": "livre",
    "suraj": "soleil"
}

# Taking English word from user
word = input("Enter an English word: ")

if word in eng_hindi:
    hindi = eng_hindi[word]
    french = hindi_french[hindi]
    
    print("Hindi meaning:", hindi)
    print("French meaning:", french)
else:
    print("Word not found in dictionary")

print("NAITIK SINGHAL")
print("")    

#Question-59

# Creating a dictionary
student = {"name": "Tanmay", "age": 18, "course": "BTech"}

# i) dict()
d = dict(a=1, b=2)
print("dict():", d)

# ii) len()
print("len():", len(student))

# iii) clear()
temp = {"x": 10, "y": 20}
temp.clear()
print("clear():", temp)

# iv) get()
print("get():", student.get("name"))

# v) pop()
student.pop("age")
print("pop():", student)

# vi) popitem()
student.popitem()
print("popitem():", student)

# vii) keys()
print("keys():", student.keys())

# viii) values()
print("values():", student.values())

# ix) items()
print("items():", student.items())

# x) copy()
new_student = student.copy()
print("copy():", new_student)

# xi) update()
student.update({"city": "Delhi"})
print("update():", student)
print("")
#print("NAITIK SINGHAL")

#Question-60

# Original dictionary
d = {"a": 1, "b": 2, "c": 3}

# New dictionary for inverted values
inverted = {}

for key, value in d.items():
    inverted[value] = key

print("Original Dictionary:", d)
print("Inverted Dictionary:", inverted)
print("")
#print("NAITIK SINGHAL")


#Question-61

# Set of even numbers from 1–10
even_set = {2, 4, 6, 8, 10}

# Set of composite numbers from 1–20
composite_set = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}

print("Even Set:", even_set)
print("Composite Set:", composite_set)

# all()
print("all() on even_set:", all(even_set))

# issuperset()
print("Is composite_set a superset of even_set?:", composite_set.issuperset(even_set))

# len()
print("Length of even_set:", len(even_set))
print("Length of composite_set:", len(composite_set))

# sum()
print("Sum of elements in even_set:", sum(even_set))
print("Sum of elements in composite_set:", sum(composite_set))
print("")
#print("NAITIK SINGHAL")


#Question-62



# Set of prime numbers (1–20)
prime_set = {2, 3, 5, 7, 11, 13, 17, 19}

# Set of odd numbers (1–20)
odd_set = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

print("Prime Set:", prime_set)
print("Odd Set:", odd_set)

# Union
print("Union:", prime_set.union(odd_set))

# Intersection
print("Intersection:", prime_set.intersection(odd_set))

# Difference
print("Difference (prime - odd):", prime_set.difference(odd_set))

# Symmetric Difference
print("Symmetric Difference:", prime_set.symmetric_difference(odd_set))
print("")
#print("NAITIK SINGHAL")

