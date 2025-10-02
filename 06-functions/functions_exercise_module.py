'''
Create a file named functions_exercise_module.py and another named functions_exercise_runtime.py.

Code and test simple functions as follows:

get_greeting that returns a greeting, e.g. G'day

get_greeting_to that accepts a name and returns G'day [name]

get_product that accepts two numbers and returns the product of those numbers

get_first that accepts a list and returns the first element

get_name that accepts a dict and returns the value assoc. with the name key**

get_circumference that accepts a radius and returns the circumference (2 * Pi * radius)
For Pi just use 3.14

time permitting, pick 3 of these functions and convert them into functions without a return statement, called print....

get_name >>> print_name

**these functions require mocked data to test
'''
def get_greeting():
    return "G'Day"

def get_greeting_to(name):
    return f"G'Day {name}"
    # return "G'Day " + name#breaks when passed a number

def get_product(num1, num2):
    return num1 * num2

def get_first(my_list):
    return my_list[0]

def get_name(my_dict):
    return my_dict["name"]

def get_circumference(radius):
    return 2 * 3.14 * radius


if __name__ == "__main__":
    # testing f-string with number value
    print(get_greeting_to("Alan"))
    print(get_greeting_to(1))
