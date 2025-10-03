# basically, there are 3 ways of importing functions froma a module
# module: a script that only holds functions and/or classes, and NOT runtime code

# WAY 1: fully-qualified (with module name)

import functions_module

# usage:
print(functions_module.greet6())

# PROS: there is no doubt ever at any point in your importing script that you are using a module function
# CONS: conversely, repeating the module name can be tedious

# WAY 2: named functions
# IMHO the best way

from functions_module import greet5, greet3, greet2

# usage:
print(greet5("Alan", 58))

# PROS: you can see excatly what's used at the top of the script
# no need for repetitive module name in each function call
# CONS: you could assume that functions which are actually imports
# are native functions, defined in the current script

# WAY 3: the wildcard
# IMHO the worst way!

from functions_module import *
# means that every function gets imported

# usage:
greet4("John")

# also with Python, we are able to REDECLARE a module function in the script
def greet4(name):
    print("Goodbye " + name)
    print("from greet4")
    print("nice knowing you!")

greet4("Alan")

# when this process is applied to BUILTIN functions
# Python refers to this as MONKEY PATCHING
# this is an anti-pattern in your architecture
# can cause many problems when code is extended
# and the patch is not provided