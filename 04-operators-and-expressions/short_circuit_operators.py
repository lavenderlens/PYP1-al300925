'''
a       b           a & b       a | b
                    a and b     a or b
True    True        True        True
True    False       False       True
False   True        False       True
False   False       False       False

single &, single | are technically binary operators
but work with boolean values too

short circuit operators and, or,
work with ANY object INCLUDING boolean values
and are said to be short-circuit
that is, if they obtain a result for the whole expression
in the first half,
they will not evaluate the second half
and will return an object, either the first or second half,
depending on rules

the rules are the same for booleans and/or other types of object
'''

# testing non-short-circuit logical operators (rare in Python)
# not returning objects but boolean values
truth = True 
falsehood = False 
print(truth & falsehood)#False
print(truth & (not falsehood))#True
print(truth | falsehood)#True
print((not truth) | falsehood)#False

# short-circuit operators
# returning things, not boolean values
print(truth and falsehood)#False BUT actually returns falsehood
print(truth and (not falsehood))#True BUT actuall returns truth

# let's substitute truthy and falsey objects for boolean values
# SHORT-CIRCUIT AND
print(truth and [])#[]
print(truth and "x")#x
# NOTE: it doesn't matter what truth value the RHS is, it always gets returned if the LHS is truthy

# SHORT CIRCUIT OR
print("x" or "")#x and doesn't give two hoots about the thing on the right
print(0 or [])#[]
print(0 or "x")#x and doesn't give two hoots about the thing on the right
