'''
Python does not natively allow us to specify the type or arguments or type of return from a function
However the docstring should be present in all rpoduction code
it is a triple-quoted string as the first thing in a function body
it annotates return type and args type
but does not enforce it
if we wish to validate parameters
we need to invoke the builtin type() function in our own function body
'''

def string_processor(a_string) -> str:
    """_summary_

    Args:
        a_string (str): a message to be processed

    Returns:
        _type_: str
    """
    # if type(a_string) == "<class 'str'>":#nope
    if type(a_string) == str:
        result = "Your message " + a_string
    else:
        result = None
    return result
    # return a_string # type hinting doesn'ta ctually DO anything

print(string_result := string_processor("one"))
print(type(string_result))#<class 'str'>

# BUT this also works with other datatypes
print(number_result := string_processor(1))
print(type(number_result))#<class 'int'>

def number_processor(any_number = 0) -> int | float:
    """_summary_

    Args:
        any_number (int | float): any whole or decimal number (not complex)

    Returns:
        int | float: the number given plus one
    """
    if type(any_number) == int or type(any_number) == float:#use or rather than |
        result = any_number + 1
    else:
        result = None
    return result
    # any_number += 1
    # return any_number

print(number_processor(1.0))
print(number_processor())#default named parameter enables no args version to work
# but doesn't provide any type safety/checking
print(number_processor("1"))