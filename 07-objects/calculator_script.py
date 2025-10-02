from calculator_procedural import add, sub, mul, div, equals
from calculator_oo import Calculator

add(5)
sub(2)
mul(3)
div(9)
#expected 1.0
print(equals())#1.0

calculator = Calculator()
calculator.add(5)
calculator.sub(2)
calculator.mul(3)
calculator.div(9)
print(calculator.equals())

# at this level, there may seem no obvious advantage to using classes over functions
# BUT
# have a think about the global variable total, from the procedural module
# ALL and ANY function call sees the same variable.
# whereas, in the OO version, EACH and EVERY instance of the class gets its own copy
# thus the total prop in each OO instance is encapsulated (data protected) from any others
# with the procedural code, gloabal total RESETS. after each call of the equals(0 function
# BUT in between, two scripts could both access the gloabl variable at the same time
# the class Calculator encapsulates its state for every instance
