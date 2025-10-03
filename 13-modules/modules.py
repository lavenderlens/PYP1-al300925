'''
modules are scripts imported for use in other scripts
packages are collections of modules (or sub-packages):
folder containing module scripts has an __init__.py file - 
NO contents, just __init__.py file created

there is a variant package called namespace package that does not require an __init__.py file

various types of modules
1. modules with standard Python core ("batteries included")
imported by default
no need to qualify eg. print()

2. modules in standard Python core
BUT you must import them directly and optionally, for example re (regular expressions)

3. modules you typically install on the command line using a package manager such as pip
from Python Package Index directory https://pypi.org
eg. conda by anaconda popular for data science

4. modules that we create and, optionally, open source
'''

import json

# write to json

books = [
    {"title":"The gruffalo", "author":"Julia Donaldson"},
    {"title":"Scary Smart", "author":"Mo Gawdat"},
    {"title":"Born To Run", "author":"Bruce Springsteen"},
]
print(books)

# PYTHON => JSON
print(books_json := json.dumps(books))
print(type(books_json))#str

# JSON => PYTHON
print(books_from_json_into_python := json.loads(books_json))

