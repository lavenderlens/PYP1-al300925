"""
   from a user POV, exception handling enables the code to recover
   and carry on from a catastrophic event
   from a dev POV, it enables us to create and raise Errors 
   (objects with information about the problem)
   according to business logic 
   exceptions should be seen as creating opportunities
   (for our system to intervene)
   not so much as presenting difficulties
"""

num1 = input("Enter a number:")
num2 = input("Enter another number:")#these lines will never fail

try:
    num1 = int(num1)
    num2 = int(num2)#these lines may well fail
    # ZeroDivisionError: division by zero
    result = num1 / num2
except ZeroDivisionError:
    print("cannot divide  by zero")
    # the ORDER of multiple except blocks can matter
except ValueError:
    print("wrong input try again")
finally:
    print(result)

# stuff occurs, you do not know until runtime what that will be
# you are not required to handle these exceptions
# but should code to avoid them

try:
    nums = [1,2,3]
    print(nums[3])#IndexError: list index out of range
except IndexError:
    print("list index out of range")

print("Carrying on as usual...")