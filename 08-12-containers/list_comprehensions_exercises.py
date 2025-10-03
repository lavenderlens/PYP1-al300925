names = ["Attila", "Vishnu", "John", "Marc", "alan", "tim", "Horatio", "Alan", "Alannah"]

# using list comprehensions,
# tell me

# 1. the names of less than 5 characters length
print(short_names := [name for name in names if len(name) < 5])

# 2. the names of greater than 5 characters length
print(short_names := [name for name in names if len(name) > 5])

# 3. the names with even numbers of characters
print(even_values := [element for element in names if len(element) % 2 == 0])

# 4. the names beginning with "A" - case-insensitive, use startswith() method of str()
print("names starting with \"a\"")
print(names_starting_with_a := [name for name in names if name.startswith(("a","A"))])
print(names_starting_with_a := [name for name in names if name.casefold().startswith("a")])

# 5. all the names, upper-cased
print(all_names_upperd := [name.upper() for name in names])
# 5A. all the A-names, upper-cased
print(all_A_names_upperd := [name.upper() for name in names if name.casefold().startswith("a")])
# JS note: we have to decide in JS which comes first, map or filter


