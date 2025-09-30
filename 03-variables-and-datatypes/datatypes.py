# the standard, built-in datatypes
# literals, or single values, OR expressions that evaluate to them
# IMMUTABLE by default
# this means that a value IS a value and will always be
# we may go off and reference ANOTHER value
# but the original one doesn't change, it is merely de-referenced

# declared and initialised:
# Python variables almost always have to be initialised
# there are two exceptions for specialist edge cases
my_int = 1
# re-assigned (exactly the same syntax!)
my_int = 2
my_int = "The number two"#dynamic typing

bool = True #bool is a reserved keyword!!
# built-in function
# this is allowable but specific to my code only!
# so it's an anti-pattern called monkey-patching
print(bool)
my_bool = True
my_bool = False

# because there is NO KEYWORD to denote a variable declared for the first time
# we must always (almost always) assign an initial value which determines a variable's type as well

# int. or integer/whole number value
# values: whole numbers, negative or positive, OR an expression that evaluates to a whole number
# immutable type (values cannot be changed, just de-referenced / re-referenced)

# float. or floating-point/decimal number value
# values: fractional numbers, negative or positive, with the dot character OR an expression that evaluates to a number
# immutable type (values cannot be changed, just re-referenced)

my_float = 1.0
my_float = 1.5

# str (strings)
# values: any characters of zero or more
# immutable type
# single, double OR triple-quoted
# zero indexed (from first character)
# have a length property, obtained by using len()

my_str = "Hello"
first_character = my_str[0]
print(first_character)
print(len(my_str))
# print(len(my_str[5]))#IndexError: string index out of range

# string methods work on strings and return a NEW string
print(my_str.upper())
print(my_str)#original unchanged
# if we WANT to re-assign modified value
my_str = my_str.upper()
print(my_str)

# the walrus operator assigns and returns at once
# print(my_str = my_str.lower())#TypeError: print() got an unexpected keyword argument 'my_str'
print(my_str := my_str.lower())#TypeError: print() got an unexpected keyword argument 'my_str'
# the assignment has taken place in the parameters to print()
print(my_str)

# container types for multiple values
# LIST list() OR [] INSTANTIATED
# holds multiple values
# values may be of same type but strictly do not have to be
# mutable by default
# commonly used for items of same type
# ordered, permits duplicates

my_list = [0, True, "Hello"]#permissible but not beneficial
my_list = ["bat", "ball", "gloves"]

# copying (reference only)
my_list_copy_by_reference = my_list
# no new [] - no new object created
my_list_copy_by_reference[0] = "cricket bat"
print(my_list)#original mutated ['cricket bat', 'ball', 'gloves']

# adding elemnt to end of list
my_list_copy_by_reference.append("whites")
print(my_list)#original mutated ['cricket bat', 'ball', 'gloves', 'whites']

# TUPLE tuple() OR () INSTANTIATED
# holds multiple values
# values may be of same type but strictly do not have to be
# IMMUTABLE by default:
# does not permit ITEM re-assignment
# commonly used for items of differing type
# ordered, permits duplicates

my_tuple = ('cricket bat', 'ball', 'gloves', 'whites')
# my_tuple[3] = "cricket whites"#TypeError: 'tuple' object does not support **item** assignment
my_tuple = ("goal", "football", "boots")#lets us substitute an OVERALL different value
# tuples commonly used to store data of different types say, for instance
# the different columns of a database
# much more common with tuple rather than list
my_restaurant = ("at the end of the universe", 42, True)

# SETS
# values: the elements can be of any type
# sets are NOT ORDERED
# sets may NOT contain duplicates
# set methods are powerful ways of examining sets and returning differences and similarities
my_set = {1,2,2,3,4,4,5}
print(my_set)#{1, 2, 3, 4, 5}

my_other_set = {"one", "two", "two", "forty_four", "ninety-one", "a-one"} 
print(my_other_set)#{'a-one', 'one', 'forty_four', 'two', 'ninety-one'}
print(my_other_set)#{'one', 'ninety-one', 'a-one', 'forty_four', 'two'}

# DICTIONARIES
# values: key: value, pairs, comma-separated
# keys: may be of any type but are commonly strings
# keys must be unique
# values: may be of any type and may be duplicated
# mutable
my_dict = {"name": "Fred", "age":21, "employed":True}
print(my_dict)

# we can also make these containers using their built-in constructor functions
my_empty_list = list()
print(type(my_empty_list))
my_empty_tuple = tuple()#NOTE there is not much point in an empty tuple!
print(type(my_empty_tuple))
my_empty_set = set()
print(type(my_empty_set))
my_empty_dict = dict()
print(type(my_empty_dict))

my_empty_curly_braces = {}
print(type(my_empty_curly_braces))#<class 'dict'>
#

# None
# the value None (null in other languages) is a type itself
print(type(my_dict))#<class 'dict'>
my_dict = None
print(type(my_dict))#<class 'NoneType'>
