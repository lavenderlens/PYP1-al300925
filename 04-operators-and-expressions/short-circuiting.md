## Short-circuit operators in Python

### `or` operator

If both sides for an `or` expression evaluate to booleans the result is true if one or more sides are true. Nothing odd there.

If one or both sides are OBJECTS, then the `or` expression evaluates to an object, not a boolean.

If first side is truthy, it becomes the result, otherwise second side becomes the result. Regardless of whether second side is truthy or falsey!

### `and` operator

If both sides for an `and` expression evaluate to booleans the result is true only if both sides are true. Nothing odd there.

If one or both sides are OBJECTS, then the `and` expression evaluates to an object, not a boolean.

If first side is truthy, the second side becomes the result, regardless of whether it is truthy or falsey, otherwise first side becomes the result.

###

    in the following code "x" is truthy and both "" and [] are falsey

```python
>>> "x" or ""
'x'
>>> "" or []
[]
>>> "x" and ""
''
>>> "" and []
''
>>>
```

At first less readable than an IF- ELIF- ELSE we can leverage the behaviour of the short-circuit operators in many handy ways eg. passing in default values:

```python
name = input("Enter your name: ") or "friend"
print(f"Hello {name}")
```

If nothing is entered at the prompt, the left hand side is falsey. So Python evaluates the RHS, which gets assigned to the variable.

If a name is entered, the LHS is truthy so it gets evaluated and assigned to the variable.
