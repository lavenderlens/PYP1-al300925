'''
functions, as in any other language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
functions are commonly defined in a script ON THEIR OWN, with no runtime code
the script with the runtime code in it, that USES the functions,
is separate, and IMPORTS them from the first script
the first script is called a module

how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can a function be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
if a function consistently produces the same result for the same given input
it is said to be pure, or idempotent 
pure functions are much easier to test in an automated test environment
we do not have to mock dependencies that may change independently of the function
'''

# functions have input, output, both, or neither
# a print statement is NOT considered output
# a return statement is
# this output may be persisted in a variable
# or passed as INPUT to ANOTHER function
# input is taken in via parameter brackets ()
# even if there is no input the brackets must be there 
# both at function definition time and at runtime
# inside the brackets data is referred to as 
# PARAMETERS at function definition time
# ARGUMENTS (args) at runtime

# WAY 1. No input, no output

def greet1():
    print("Hello")

# nothing to do with function!
print("from greet1")
print("how are you today?")

greet1()

'''output:
from greet1
how are you today?
Hello
'''

def greet1():
    print("Hello")

    # belonging to the function
    print("from greet1")
    print("how are you today?")

greet1()

# wAY 2. No input, output
def greet2():
    return "Hello \nfrom greet2 \nhow are you today?"

print(greet2())

# WAY 3. input and output
def greet3(name):
    return f"Hello {name} \nfrom greet3 \nhow are you today?"

# print(greet3())#TypeError: greet3() missing 1 required positional argument: 'name'
print(greet3("Alan"))#TypeError: greet3() missing 1 required positional argument: 'name'

# WAY 4.  Input, no output
def greet4(name):
    print(f"Hello {name}")
    print("from greet4")
    print("how are you today?")

greet4("Graham")

# positional vs named args
# consider a function that accepts two positional args
def greet5(name, age):
    return f"Hello {name}\nfrom greet5\nyou are {int(age) + 1} next birthday"

print(greeting5 := greet5("John", 21))
# print(greeting5 := greet5(21, "John"))#problem!
# order MATTERS!

def greet6(name="friend", age=21):
    return f"Hello {name}\nfrom greet5\nyou are {int(age) + 1} next birthday"

print(greeting6 := greet6(name="Nils", age = 63))
print(greeting6 := greet6(age = 63, name="Nils"))
print(greeting6 := greet6())

# order doesn't matter with named args
# args can be left blank and default values will be passed in
