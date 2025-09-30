# Python is dynamically-typed
# this means that datatypes can change during an application
# this type coercion or conversion happens implicitly in Python
# but may be called explicitly as well, on purpose
# each data type has its wrapper function of the same name

# conversion to boolean (bool)
# every datatype has its truthy and falsey values (convert to True or False)
# easier to remember the Falsey values - most values are truthy
# falsey values:
# Zero numbers 0 and 0.0
# empty collections/containers ** not so in JS
# including str which is a collection or container (of single characters)
# note empty collections in JS, by contrast, are truthy!
# None

# print("using the bool() wrapper function")
# print("numbers: ")
# print(bool(1))
# print(bool(-99))
# print(bool(0))
# print(bool(0.0))

# print("strings:")
# print(bool("Hello"))
# print(bool("H"))
# print(bool(" "))
# print(bool(""))

# print("containers: list")
# print(bool([1,2,3]))
# print(bool(["name"]))
# print(bool([]))

# print("containers: dictionary")
# print(bool({"name": "Alan", "age": 21}))
# print(bool({2: 22, 1: 33}))
# print(bool({}))#actually an empty set
# print(bool(dict()))#an empty dictionary

print("type coercion using the str() wrapper function")
print(str(True))
print(str(False))
# note both values True and False evaluate as True booleans
if str(True):
    print("value True evaluates as boolean True")
if str(False):
    print("value False ALSO evaluates as boolean True")
# this is because both are NON-EMPTY string swhen passed to the str() wrapper

print("type coercion using the int() wrapper function")
print(int(True))#1
print(int(False))#0

print("float to int: a DOWNCAST, bigger into smaller type")
print(int(1.0))#1 - float to int
print(int(1.9))#1 - float to int

print("int to float: an UPCAST, smaller type into bigger type")
print(3/4)#0.75