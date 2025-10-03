'''
sets are UNordered, mutable containers that do not permit duplicates
as such, they are often used for converting lists with duplicates into unique values
more than this, they have many utility methods for comparing sets, useful for data science
'''

# creation
nums = {4,5,6,4,5,6}
empty_nums = set()#NOT an empty dict which is {}
print(type(empty_nums))#set
print(nums)#{4, 5, 6}

names = ["Attila", "Vishnu", "John", "Marc", "alan", "alan", "tim", "tim", "Horatio", "Alan", "Alannah"]
names_as_set = set(names)
print(names_as_set)
#{'alan', 'Vishnu', 'Attila', 'Marc', 'John', 'Alan', 'Alannah', 'tim', 'Horatio'}
#'John', 'Alan', 'Attila', 'Horatio', 'Vishnu', 'Marc', 'Alannah', 'alan', 'tim'}

print("# common use: filter out duplicates")
list_with_dupes = [1,2,3,1,2,3]
unique_nums = set(list_with_dupes)
print(type(unique_nums))
print(unique_nums_as_list := list(unique_nums))
print(type(unique_nums_as_list))

# comparing sets
nums1 = {55,66,44,55,66,44}
nums2 = {55,66,33,22,11}

# values in common to both sets
print(common_values := nums1.intersection(nums2))#reflexive
print(common_values := nums2.intersection(nums1))#reflexive

# difference of 2nd set from 1st
print(different_values := nums1.difference(nums2))#non-reflexive
# difference of 1st set from 2nd
print(different_values := nums2.difference(nums1))#non-reflexive
# all differences between both sets
print(all_different_values := nums1.symmetric_difference(nums2))#reflexive{33, 22, 11, 44}
print(all_different_values := nums2.symmetric_difference(nums1))#reflexive{33, 11, 44, 22}
