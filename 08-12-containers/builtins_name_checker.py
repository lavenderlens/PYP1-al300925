'''
how do we know if a variable or function name we choose is already reserved?
we don't. I could stand corrected on this.
# str = "str" #the system reserved word str is now monkey-patched to a different meaning
# my_str = str()#this line will fail
task: to build a python program for checking if our word is a reserved word.
'''

all_builtins = dir(__builtins__)
# print(all_builtins)
# print(type(all_builtins))
# all_builtins_list = [ name for name in all_builtins]#already a list

my_name = input("Enter a name to try:")#testing
print(f"SEARCHING {my_name} in top-level builtins...")
for name in all_builtins:
     if name == my_name:
          print("ERROR, ALREADY A BUILTIN NAME")
          break
    #  else:
    #       print("PASS: original name")#this will print a LOT of passes!
else:
    print(f"{my_name} not found in top-level builtins, all good")
     
recursive_builtins = []
for name in all_builtins:
    if not name.startswith("__"):
        subdir = dir(name)
        for name in subdir:
                if not name.startswith("__"):
                    recursive_builtins.append(name)

print("\\recursively:")
# print(recursive_builtins)

print(f"SEARCHING {my_name} recursively in all builtins subdirectories...")
for name in recursive_builtins:
     if name == my_name:
          print("ERROR, ALREADY A BUILTIN NAME IN A SUBDIRECTORY")
        #   could also use sets
          break
else:
    print(f"{my_name} not found in any subdirectory, all good")