def greet1():
    print("Hello")
    print("from greet1")
    print("how are you today?")

def greet2():
    return "Hello \nfrom greet2 \nhow are you today?"

def greet3(name):
    return "Hello " + name + "\nfrom greet3 \nhow are you today?"

def greet4(name):
    print("Hello " + name)
    print("from greet4")
    print("how are you today?")

def greet5(name, age):
    return f"Hello {name}\nfrom greet5\nyou are {age} today"

def greet6(name="friend", age = 21):
    return f"Hello {name}\nfrom greet6\nyou are {age} today"
