def greet7(name, languages):
    return f"My name is {name} and I train {languages}"

print(greet7("Alan", ("Python", "JavaScript")))#multiple elements as a single argument

# this poses a question about what data exists when;
# does it make sense in our buisnes for a list of languages to exist before being assigned to a trainer?
# this affects objects and classes more than it does functions on their own
# aggregation or composition?
# an aggregate relationship is where the subordinate (the part) may exist independently (and before) the superordinate (whole)
# a compositional relationship exists where the subordinate may not exist outside of the superordinate
# business logic usually leaves it entirely up to which to code to
# for instance it might be sensible for a separate languages list to exist 
# if it is shared between trainers and the training company

# *args
# the * is mandatory, the args is not
# none, one, or many args are packed into a tuple
# the *args parameter must come after any others

def greet8(name, *languages):
    return f"My name is {name} and I train {languages}"
my_languages = ("Python", "JavaScript")
# print(greet8("Alan", my_languages))#multiple elements as a single argument
print(greet8("Alan", "Python", "JavaScript", "Java"))#multiple elements as individual elements
# *args will pack n number of args from zero to many into a tuple
# the use of a tuple is of note:
# if you wished to update or modify your languages after the function is called then you wouldn't use it
# as tuple does not permit item re-assgnment
# again, this is more relevant for functions within classes

# **kwargs
# any number of named keyword arguments packed into a dictionary
# the ** is mandatory, the kwargs is not
# none, one, or many keyword args are packed into a dictionary
# the **kwargs parameter must come after any others INCLUDING *ARGS IF PRESENT

def greet9(name, *languages, **address):
    return f"My name is {name} and I train {languages}, I live in {address}"

print(greet9("alan", "react", "css", county="Donegal", country="Ireland"))




