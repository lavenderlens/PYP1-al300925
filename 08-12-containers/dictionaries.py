'''
a dictionary is a mutable, UNorderd container of key: value pairs
KEYS must be unique: values need not be
dicts are commonly used to represent complex data
and to facilitate sharing between different languages in any stack
eg. JavaScript > JSON > Python > Java

use a class where you want a uniform list of props and functions that modify those props
use a dict where you have a one-off scenario or props/data shape may change
'''

# creation
book1 = {}#empty dict - # caveat for empty set use set constructor
book2 = dict()#empty dict
print(type(book1))
print(type(book2))

# adding props is possible AFTER instantiation
# not possible with classes and objects
book1["title"] = "Scary Smart"
book1["author"] = "Mo Gawdat"
book1["published"] = 2019

# is this a win on number of LOC?
# No, a dictionary with props at instantiation time would also be 4 LOC
book3 = {
    "title": "Scary Smart",
"author" : "Mo Gawdat",
"published": 2019
}

# in a class:
class Book:
    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published
    def __str__(self):
        return f"{self.title}, {self.author}, {self.published}"
book4 = Book("Why We Drive", "Matthew Crawford", 2021)
# so it may seem on the surface we have more code for a class
# BUT we can re-use the class (see Calculator, /classes-and-objects section)
# if we want another dict we have to code individually
book5 = {
    "title": "Why We Drive",
"author" : "Matthew Crawford",
"published": 2021
}
# if we want another instance of a class, we only need call ONE LOC
book6 = Book("Born to Run", "Bruce Springsteen", 2018)

# objects from classes have same attribute names baked in
# dictionaries do not guarantee same attribute names
# dictionaries: less code to start with, but all needs repeated each time
# fragile over large datasets

# iterating over dicts
# values (JS equivalent of for OF loop)
for value in book5.values():
    print(value)

# keys
for key in book5.keys():
    print(key)

# in the absence of any method above, a loop will return the keys
# this IS like the for - in loop in JS
for key in book5:
    print(key)

# keys and values together
for key, value in book5.items():
    print(key, value)
    print(type(key))
    print(type(value))

    
