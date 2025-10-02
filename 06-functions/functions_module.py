def greet1():
    print("Hello")
    print("from greet1")
    print("how are you today?")

def greet2():
    return "Hello \nfrom greet2 \nhow are you today?"

def greet3(name):
    return f"Hello {name} \nfrom greet3 \nhow are you today?"

def greet4(name):
    print(f"Hello {name}")
    print("from greet4")
    print("how are you today?")

def greet5(name, age):
    return f"Hello {name}\nfrom greet5\nyou are {int(age) + 1} next birthday"

def greet6(name="friend", age=21):
    return f"Hello {name}\nfrom greet5\nyou are {int(age) + 1} next birthday"

# IF we have procedural code in the module 
# it will ALWAYS RUN in any importing script
# and it will run BEFORE any function calls
print("FUNCTIONS MODULE")

# if we MUST write procedural code in a module,
# we may hide it from any importing script by putting it behind THIS:
if __name__ == "__main__":
    # if the name of this script is the script that is running in the interpreter
    print("I am runtime code in the module")