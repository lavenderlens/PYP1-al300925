'''
a list is a mutable, indexed/ordered container
permits duplicates
commonly used to store elements of the same type (any)
but need not be
'''

# creation
nums = []
nums = list()#empty list
nums = [1,2,3]

# element referencing
print(third_element := nums[2])

# element reassigning
nums[2] = 4

# adding elements (to the end of list)
nums.append(5)

# obtaining the implicit length prop
print(len(nums))
print(nums)#[1, 2, 4, 5]

# slicing: the creation of a new list from all or some parts of the original
# slice syntax:
# [startIdx, endIdx, step]
# note endIdx is EXclusive (one beyond what you need)
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))#10
# print(fib[10])#IndexError: list index out of range

# using list slicing, give me
# the last 5 values
print(fib[5:])
# the first 5
print(fib[0:5])#endIdx is EXclusive (one beyond)
# the last element
print(fib[9:])
print(fib[9:10])#endIdx is EXclusive (one beyond)

# the main point:
print(fib)#unchanged

# the third arg: step
# give me every second value
print(fib[::2])#note for 3rd arg fist two must be specced or : inserted
# every second value missing out first value
print(fib[2::2])
# reverse step
print(fib[::-1])

# this is powerful but depends on a knowledge of index
# what if we could perform analysis like this but knowledge of index is NOT required?
# in other words, the element itself is questioned?

# list comprehensions are a powerful tool that do not depend on the index
# a comprehension passes in a function
# to be performed on every element of the original list

# get the actual even number values
print(even_values := [element for element in fib if element % 2 == 0])
# could have done this:
even_values = []
for element in fib:
    if element % 2 == 0:
        even_values.append(element)

# odd values
print(odd_values := [element for element in fib if element % 2 != 0])
print(odd_values := [element for element in fib if element % 2 == 1])
# values under 10
print(values_under_ten := [element for element in fib if element < 10])
# similar to a filter operation
# passes in a function containing a predicate or a test against which every element is matched
# those that pass the test make it the new list
# those that don't dont't.

# akin to a map operation is a list comprehension where a transform is applied for EVERY element
print(values_squared := [element * element for element in fib])
print(values_scaled_by_2 := [element * 2 for element in fib])

# inserting before an index
names = ["Attila", "Vishnu", "John", "Marc", "alan", "tim", "Horatio"]

names.insert(4, "Bertrand")
print(names)

# deleting elements
del names[4]
print(names)

# if we don't know the index
del names[names.index("alan")]
print(names)

# remove last element, returns element also
print(horatio := names.pop())
print(names)

# remove from an index
print(tim := names.pop(names.index("tim")))
print(names)

# membership operator
print("John" in names)
print("Jon" in names)

names.append("James")
# default sort
names.sort()
print(names)
# reverse sort
names.sort(reverse=True)
print(names)
# sort by length
names.sort(key=len)
print(names)