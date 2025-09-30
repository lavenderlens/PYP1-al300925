# the input() function takes keyboard input from the user
# there are of course IRL many more forms of input device
# in development and testing we tend to stick with keyboard in: terminal out

print("Enter your name:")
name = input()#declared and initialised from input() - NO KEYWORD!!
# there is NOTHING to distinguish when a variable is FIRST declared
# from when it is RE-ASSIGNED
name = "Bruce Springsteen"#re-assigned
print(type(name))#<class 'str'>
name = 1#dynamic typing: datatypes cand and do change during an application
print(name)
print(type(name))#<class 'int'>
# we can find out the datatype by the built-in type() function

# the input function is a built-in, as is print() and type()
# we can inspect the built-ins on the command line

# input function ONLY EVER returns a string
# if we wish to coerce inut into a different datatype we must perform a conversion AFTER the input is gathered

number1 = input("Eneter a number")
number2 = input("Eneter another number")
print(int(number1) + int(number2))

# TODO write a Python script to check if a variable name is already in the built-ins (at top level only for starters)
