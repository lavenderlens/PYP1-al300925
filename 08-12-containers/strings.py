'''
strings are immutable, ordered containers of characters
they may contain duplicates
string methods return a NEW string
the original is unaffected but the same reference may be updated
to point to the new string instead
'''

s1 = "Hello"
s2 = "Hello"
print(s1, id(s1))#Hello 4338184864 / 4378768032 / 4378456736
print(s2, id(s2))#Hello 4338184864 / 4378768032 / 4378456736

s3 = str("Hello")
s4 = str("Hello")
print(s3, id(s3))#Hello 4338184864 
print(s4, id(s4))#Hello 4338184864 

# NOT analogous to JS / Java String pool memory

# in Python, EVERYTHING is an object
# objects of type str have their __eq__ method overridden to say
# if they are the same characters in the same order, they must be equal

l1 = ["Hello"]
l2 = ["Hello"]
print(l1, id(l1))#['Hello'] 4308727872
print(l2, id(l2))#['Hello'] 4308568256 #different!
print(l1 == l2)

# while everthing is an object, so lists are an object
# they are a mutable type of object
# and also provide an implementation of __eq__
# they are MUTABLE
# strings are IMMUTABLE
# if a value is immutable its id() will be the same as another
# you can't change the object so it is safe to assign the same id
# if a value is mutable its id() will be different to another
# you may change the object so it is UNsafe to assign the same id
# mutable container types may contain immutable objects like strings, numbers

# raw strings
# sometimes escape characters need to be printed literally
# eg. in a file path C:\Users
# print(file_path := "C:\users")#SyntaxError: (unicode error) - \u denotes a Unicode character following
# \u is escape code for Unicode character references

print(file_path := r"C:\users")#raw string - will ignore escape characters

print(registered_symbol := '\u00ae')
print(waving_hand := '\U0001F44B')
print(dog_face := '\U0001F436')
print(f"the unicode escape for a dog face is {'\U0001F436'}")
print(f"the unicode escape for a dog face is {r'\U0001F436'}")


