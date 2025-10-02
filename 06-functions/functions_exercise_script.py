from functions_exercise_module import (get_greeting_to, 
get_circumference, get_first, get_greeting, get_name, get_product)

print(f"get_greeting {get_greeting()}")
print(f"get_greeting_to {get_greeting_to("Alan")}")
print(f"get_product {get_product(2, 2)}")
print(f"get_first {get_first([1,2,3])}")
my_dict = {"name": "Fred", "age":21}
print(f"get_name {get_name(my_dict)}")
print(f"get_circumference {get_circumference(10):.2f}")
