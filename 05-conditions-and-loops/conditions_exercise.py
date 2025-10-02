# Part 1 Conditionals
# In this exercise you will create a script that prompts the user to input his/her birth year,
# and then prints to the console the generation of which he/she is a member, e.g. Baby
# Boomer, Generation X, etc.
# 1. Create a script named conditionals_exercise.py.
# 2. Prompt the user to input his/her birth year and capture it in a variable named
# birth_year.
# 3. Convert birth_year to an int.
# 4. If the user was born between 1946 and 1965, print Baby Boomer to the console.
# 5. If the user was born between 1966 and 1976, print Generation X to the console.
# 6. If the user was born between 1977 and 1994, print Millennial to the console.
# 7. If the user was born in 1995 or beyond, print Generation Z to the console.

# birth_year = int(input("Enter the year you were born:"))
birth_year = input("Enter the year you were born:")#an error will never occur here
birth_year = int(birth_year)#an error could occur here

if birth_year >= 1946 and birth_year <= 1965:
    print(f"Born in: {birth_year}: baby boomer!")
elif birth_year >= 1966 and birth_year <= 1976:
    print(f"Born in: {birth_year}: Gen X!")
elif birth_year >= 1977 and birth_year <= 1994:
    print(f"Born in: {birth_year}: Millenial!")
else:
    print(f"Born in: {birth_year}: Gen Z!")

# OR, using upper bounds only
if birth_year < 1946:
    print("too old to categorise")
elif birth_year <= 1965:
    print(f"Born in: {birth_year}: baby boomer!")
elif birth_year <= 1976:
    print(f"Born in: {birth_year}: Gen X!")
elif birth_year <= 1994:
    print(f"Born in: {birth_year}: Millenial!")
else:
    print(f"Born in: {birth_year}: Gen Z!")

# OR, using a builtin
if birth_year in range(1946, 1966):
    print(f"Born in: {birth_year}: baby boomer!")
elif birth_year in range(1966, 1976):
    print(f"Born in: {birth_year}: Gen X!")
elif birth_year in range(1977, 1994):
    print(f"Born in: {birth_year}: Millenial!")
else:
    print(f"Born in: {birth_year}: Gen Z!")