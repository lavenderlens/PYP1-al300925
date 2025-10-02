# basically, there are 3 ways of importing functions from a module
# module: a script that only holds functions and/or classes, and NOT runtime code

# WAY 1: fully-qualified (with module name)

import functions_module

# usage:
print(functions_module.greet6())

# PROS: there is no doubt ever in your importing script that the function originates somewhere else
# CONS: repeating the module name acan be tedious

# WAY 2: named imports
# the best, IMO

from functions_module import greet5, greet3, greet2

# usage:
print(greet5("Alan", 59))

# PROS: you can see exactly what's used at the top of the script
# no need for repetitive module name in each function call
# CONS: you could assume that functions which are actually imports
# are native functions, defined in the current script

# WAY 3: the wildcard
# UNLESS you are using ALL functions from a module, the worst way IMO

from functions_module import *
# means every function gets imported

# usage
greet4("John")

# PROS: easy and quick for development
# if you MUST use this way, consider swapping it for one of the others
# when re-testing for production code
# CONS: the next dev cannot see which functions are in the module
# or which functions are used in the script
# when a function is called from the module
# it looks identical to a function call from the script