# Introduction to the Python language

## Introduction and History

Python: _NOT_ named after snakes, but the Monty Python TV show.

Guido van Rossum, Python's creator, was huge fan.

Object-oriented, high-level language, arguably easier to learn than Java.

High-level languages are DECLARATIVE rather than imperative.

Java:
System.out.println("Hello World")

Python:
print("Hello World")

We don't specify so much HOW to do something, just say WHAT to do.

OO languages:
Favour data encapsulation in object structures. For Python, the DICTIONARY structure is akin to a LITERAL object in JavaScript

JS: object literal

    {
        name: "Alan",
        age: 58
    }

JSON:

    {
        "name": "Alan",
        "age": 58
    }

PY dict:

    {
        name: "Alan",
        age: 58
    }

Objects syntax: key: value pairs, comma separated, enclosed in curly braces {}

Objects use case: They wrap **RELATED** state (variables) and behaviour (functions) into one data structure.

Objects are MUTABLE by default.

As a complement not a alternative to OOP is FP (Functional Programming)

## Functional Programming

IMMUTABLE data preferred, data may not change in ways OOP allows.

THINK OF OOP: "SAVE" on a Word doc
THINK OF FP: "SAVE AS" on a Word doc

NEITHER OOP NOR FP are exclusive! They both play nice together.

## Python versioning

Python was re-written between versions 2 and 3. Strangely for a language, this was a BREAKING CHANGE. Code written in 3 > will not run on the 2 interpreter.

Most of what we do hasn't changed since version 3.5. But best to install latest version on your own machines from python.org/downloads.

Once installed, run two ways:

1. Interactive mode: as REPL shell (Read, Evaluate, Print, Loop) - one line at a time, interactively in Terminal/Command Line.

2. In Script mode - write in an editor, such as VS Code, save with the .py extension, run in editor or from command line.

We will mainly be writing in script mode to persist our code. However I would encourage you to play around with REPL shell code as we go, to unit test small chunks of code.

## Implementations

A Python implementation is not something we should concern ourselves with as it is to do with the underlying language.

Python code, using the standard implementation of CPython (underlying written in C) is interpreted - ie. there is NO separate compile-time stage to check for syntax errors. No performance optimisation at low-level machine code, but the IDE can still help us with hints/suggestions (called linting).

## Editors

PyCharm, Spyder, Idle (after Eric Idle), used to ship with Python install, Visual Studio (FULL version, paid for and community edition .net environment for MS Sharepoint devs), Visual Studio Code (Open source, used for this course), IntelliJ IDEA, Webstorm, Eclipse, Sublime, Atom.

We use VS Code as it is fully featured and fully open source.

## Documentation

The Python official docs are intended for those who already have a proficiency in coding, and can be quite hard to read for a beginner. They are excellent for those whom Python is not their first language.

Fortunately there are several alternatives. W3Schools.com is excellent for learning access across many langauges, and GeeksForGeeks.org is excellent for looking up things as you go. GFG is curated individual contributors. More in depth than W3Schools but not as much as Python official docs.

If you want to search a particular function or feature try combining it in your search string with "W3" or "geeksforgeeks" - that will give you a deep link.

## Naming conventions

Variables and functions should be named snake_case.

Classes, by contrast, should be named PascalCase (CamelCase).

If you EVER see a capital letter in Python, there should be a class associated with that.

Python does not support constants as such (variables that may not be reassigned). BUT should indicate that something be treated _as if it were a constant_ by SCREAMING_SNAKE_CASE.

Comments should be whole sentences, Sentence case. Terminated with a full stop and two spaces. Delineated with a hash character at the start of each comment line

#Yes, the spec is that fussy.

```python
'''Triple-quoted comments have a special use case inside functions.
But may also be used for multi-line comments
'''
```

All these are BEST PRACTICE, and flouting them doesn't mean your code won't run, but adhering to them is better readability for experienced Python devs.

## Indenting and line-splitting

Indents are fundamental in Python and denote code blocks (LOC belonging to a particular statement).

Each statement in Python is delineated by the newline character.

You CAN have semi-colons to put multiple statements on one line, but this is not encouraged.

eg.

num1 = 1; num2 = 2

splits should happen if line length exceeds 89 characters or before

Note that modern practice may override this eg. UK Government recommends line length of 120 characters.

```python
#3 ways to split:

technology_without_an_interesting_name = "TWAIN"

technology_without_an_interesting_name =
\"TWAIN"

{technology_without_an_interesting_name =
"TWAIN"}

(technology_without_an_interesting_name =
"TWAIN") #best IMO.
```

See also the Walrus operator for return as well as assign.
