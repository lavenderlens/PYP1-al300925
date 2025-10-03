'''
a tuple is like a list whose members may not be re-assigned
as such, it is suitable for representing small amounts of
heterogeneous data (of different sorts)
often the result of a function
it is ordered
may permit duplicates
'''

# creation
my_tuple = ("Alan", 21, ["walking", "photography"], True)
my_empty_tuple = tuple()#what's the point!
# item assignement/re-assignment not permitted

fib = (0,1,1,2,3,5,8,13,21,34)

# tuple methods
print(fib.count(1))
print(fib.index(21))

# we may perform tuple slicing AND tuple comprehensions
# slicing returns a new tuple
print(high_numbers := fib[7:])#(13, 21, 34)
# tuple comprehensions return a new LIST
print(over_20s := [el for el in fib if el > 20])#[21, 34] #LIST

# tuple arithmetic
print(fib + (55,89))
print(fib * 2)
# to multiply each element by 2 we need a comprehension

# iterating
for el in fib:
    print(el)

# enumerating indices and values:
for index, value in enumerate(fib):
    print(index, value)