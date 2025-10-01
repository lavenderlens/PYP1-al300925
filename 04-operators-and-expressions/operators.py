# an expression involves operators (symbols that perform operations) 
# and operands (values that are transformed by the operator)
x = 1 #declares variable named x that is assigned int value of 1
x = x + 1 #re-assigns new value of itself plus one to x
# the first line initialises x with a single value, 1
# the second line assigns x the result of an expression - itself plus 1
# the expression has an operator, +
# and two operands, x (again), and 1
# single = in programming is always assignment never comparison

# arithmetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 ** 3 is 2 cubed
# /
# %     - remainder, whole number division
# //    - quotient, whole number division

'''
1       0       1       1
8               2       1 //binary 11

// multiply 11 by 2

1       0       1       1       0
16              4       2        //binary 11

floating point innacuracy occurs due to converting numbers to binary
and performing a binary shift to calculate result
'''
print(10/2)#5.0 - the result of divided two ints is promoted to a float
print(10 % 2)#0
print(10 % 3)#1
print(10// 2)#5
print(10// 3)#3

print(10/3)#3.3333333333333335
# 80s standard for floating point division
# IEEE754
# we should not use floating-point values where accuracy is important
# we could format our output:
print(f"formatted output: {(10/3):.2f}")

# promotion (smaller type into larger type)
print(10/2)#5.0
print( 9 + 2)#11 (int)
print( 9 + 2.0)#11.0 (float)

# non-numeric arithmetic
print("ho" * 3)
print("*" * 50)
# the mechanism underlying this is special method of the str class 
# that overrides the default object class behaviour of how * should behave
# * has standard implementations in number classes as with other languages
# Python also implements it for strings

# assignment operators
# = is single assignment
# += is compound assignment
# note these work for strings and numbers both

my_num = 1
my_num = my_num + 1
my_num += 1
print(my_num)#3

my_str = ""
my_str += "I "
my_str += "love "
my_str += "Python. "
print(my_str)

# note this way of building strings is expensive in memory when long strings are involved
# other methods see https://www.tracedynamics.com/python-string-builder/

# walrus operator
# like a walrus lying on ts side with two eyes : and two tusks =
# assigns AND returns at once
# before:
x = 1
print(x)
# cannot do this :
# print(x=2)#TypeError: print() got an unexpected keyword argument 'x'
# can do this (after)
print(x:=3)#

# nested data with respect to tuples in particular
my_nested_dict = {
    "name": "Alan",
    "languages": ("Python", "Java", "JavaScript")
}
# tuple within dict
# tuple ELEMENTS may not be reassigned
# but the overall reference may be
# also note square brackets notation to refer to dict keys
print(my_nested_dict["languages"][2])#JavaScript
# my_nested_dict["languages"][2] = "React"#TypeError: 'tuple' object does not support item assignment
my_nested_dict["languages"] = ("English", "Irish", "French")#OK
print(my_nested_dict)

# things that ae NOT very Python-esque
# increment and decrement operators ++ and -- NOT in python

# multiple assignment on one line
x = 1; y = 2; z = 3

# much better
# x, y, z = 1, 2 #ValueError: not enough values to unpack (expected 3, got 2)
x, y, z = 1, 2, 3
print(z)

# assignment operator chaining (VERY hard to read)
x = 1
y = 1
# may be re-written
x = y = 1

# container operators
# dict

name, languages = my_nested_dict["name"], my_nested_dict["languages"]
print(name)
print(languages)
# we will see later that objects use DOT notation for props
# dictionaries use square brackets notation

# list
my_nums = [1,2,3]
first, second, third = my_nums[0], my_nums[1], my_nums[2]

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
# 3 >= 4    #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as

# the is (for identity) operator
my_nums = [1,2,3]
my_other_nums = [1,2,3]
my_nums_copy = my_nums
# using the is operator to check equality of reference
print(my_nums is my_other_nums)#False
print(my_nums is my_nums_copy)#True equality of reference / referential equality

# the system Python uses to establish if two refs point the same object is the built-in id() function
print(id(my_nums))          #4341628544
print(id(my_nums_copy))     #4341628544
print(id(my_other_nums))    #4341221568

print(my_nums == my_nums_copy)#True
print(my_nums == my_other_nums)#True

# in the list class, the method called __eq__() is overidden to say
# if two lists have the smae elements in the same order
# they are equal

# because my_nums_copy has the same referential equality as my_nums
# the original may be mutated through the copy ref and vice versa
my_nums_copy.append(4)
print(my_nums_copy)
print(my_nums)

# if we want immutable copies that do not cahnge the original
#  I could try this
my_nums_immutable_copy = [my_nums]
print(my_nums_immutable_copy)#later: see list comprehensions also for immutable copying
# but this produces a list within a list
# OR
new_nums = []
for num in my_nums:
    new_nums.append(num)

new_nums.append(5)
print(new_nums)#[1, 2, 3, 4, 5]
print(my_nums)#[1, 2, 3, 4]

import copy
# copy has two main methods copy() and deepcopy()
# the first makes immutable copies with no recursion
# the second makes immutable copies with ANY DEGREE OF recursion
my_nums_shallow_copy = copy.copy(my_nums)
my_nums_shallow_copy.append(5)
print(my_nums_shallow_copy)
print(my_nums)#original unchanged [1, 2, 3, 4]

my_nested_nums = [1,2,3,[4,5,6]]
my_nested_nums_shallow_copy = copy.copy(my_nested_nums)
my_nested_nums_shallow_copy[3].append(7)
print(my_nested_nums)#[1, 2, 3, [4, 5, 6, 7]]#still retains a ref one level of recursion down

my_nested_nums_deep_copy = copy.deepcopy(my_nested_nums)
my_nested_nums_deep_copy[3].append(8)
print(my_nested_nums)#[1, 2, 3, [4, 5, 6, 7]] original unchanged
# copy.deepcopy works for ANY level of recursions

 