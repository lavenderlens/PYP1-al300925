# 1. Create a script named exercise1_console_io.py.
# 2. Prompt the user to input his/her name and capture it in variable named name.
# 3. Prompt the user to input his/her age and capture it in a variable named age.
# 4. Print the user's name and age to the console. You might try doing this with one
# invocation of the built-in print function. Try using a string label such as "Your name: "
# Experiment with different ways of using one print statement for both variables.
# 6. Optionally, try adding 1 to the age and display it as age next birthday.

# 7. Modify your script so that the variable for age has its
# datatype changed after it is taken in from the user and before it is used in an expression.
print("Enter your name:")
name = input()
print("you entered",name)#space inserted between multiple args to print()
print("you entered " + name)#space inserted manually, string concatenated
print("Enter your age:")
age = input()
print("you entered",age)#works
print("you entered " + age)#works with age as a string
# print("age next birthday " + age + 1)#TypeError: can only concatenate str (not "int") to str

# convert age to int
age = int(age)
print("age next birthday", age + 1)#works
# print("age next birthday " + age + 1)#TypeError: can only concatenate str (not "int") to str
print("age next birthday " + str(age + 1))#works

# since Python 3.5 => placeholders
print(f"age next birthday {age + 1}")#much more readable
print(f"my name is {name} and I will be {age + 1} next birthday.")#much more readable

# since Python 3.7 => multi-line formatted strings
print(f'''
Hello {name}
next birthday
you will be
{age + 1}''')

