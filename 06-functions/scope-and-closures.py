# closures enable functions to have and remember state between successive invocations
'''
scope defines the visibility and lifespan of a variable
WHERE and WHEN it is seen / available
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   functions can see the scope chain "up and out" 
-   but not down and in
-   global scope lives whilst the whole script is executing
-   pure functions: accept copies of data, 
-   ALWAYS return the same thing EVERY time, for given same input
-   impure functions: have global dependencies on OTHER functions/variables,
-   do not always return same result for same given input
-   because their dependencies may change
-   impure functions are VERY hard to test
lexical scope:
-   defined as local function scope, lexical scope includes a "memory" of its parent function scope
-   this is achieved when a function is returned from the parent function with the local variable
-   that local variable becomes EFFECTIVELY GLOBAL for the function returned
-   lexical scope means functions can have memory and state persists between function calls

'''
# pure vs impure functions
next_num = 1 #global

# impure function
def get_next_num():
    return next_num + 1

print(get_next_num())#2
print(get_next_num())#2

# value is always the same, code does not write back to original global
# how is this not pure? I'm getting smae result each time.

next_num = 99
print(get_next_num())#100

# get_next_num has a global dependency on next_num
# easy to break output, hard to test

# make function pure:

def get_next_num_pure(any_num):#placeholder for ANY number
    return any_num + 1

print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))#100

next_num = 199

print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))#200 BUT the INPUT has changed

# global dependency STILL APPEARS to change output
# but the value of the arg copied into the pure function ALSO changes
# so the function is pure, NO global dependency as it passes by copy

# what if we wished to update global state in our function?
# we have to TWO-WAY BIND function code to global state
# we use the keyword global

# normally, any variable declared within a function is local-scoped to taht function
# even if it has same name as a global, it is a different thing

def get_local_next_num():
    next_num = 1#newly defined within the function
    next_num += 1
    # return next_num += 1#assignment in return no good
    return next_num#assignment in return no good

print(get_local_next_num())#2
print(get_local_next_num())#2
print(next_num)#199

def get_and_mutate_next_num():
    global next_num#next_num is now bound to the global of the same name
    next_num += 1
    return next_num

print(get_and_mutate_next_num())#200
print(next_num)#200
print(get_and_mutate_next_num())#201
print(next_num)#201
print(get_and_mutate_next_num())#202
print(next_num)#202

# what if we were to bind to LOCAL function scope and not to global?
# local function scope is EFFECTIVELY global to functions returned from a function
# this enables state to persist between function calls

# a variable declared inside a function is said to have LOCAL scope
# as we have seen above
# it remains completely separate from a global variable EVEN of the same name

# we can do the following because:
# functions themselves are higher order objects (HOC/HOF) in Python
# this means they can be passed to and returned from other functions
# if we have an inner function, its effectively global scope
# is the parent, or outer functions's scope
# this scope level, to an inner function, is called LEXICAL scope
# it means: the outer function scope
# EFFECTIVELY global,
# to an inner function returned

def get_next_lexical_num():
    next_num = 3001
    #   locally scoped to the outer function
    #   lexically-scoped to an inner function
    def get_and_mutate_next_lexical_num():
        nonlocal next_num#next_num is now bound to the outer function scope
        # only this inner function may mutate it's lexically-scoped variable
        next_num += 1
        return next_num
    return get_and_mutate_next_lexical_num

# inner function, when invocated as part of a function expression,
# is said to create a CLOSURE around the lexically-scoped variable
# it not only remembers the value of its lexically-scoped environment at closure creation time
# it also persists this value IN BETWEEN function calls

my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())
print(my_closure())
# the function has memory!
# to reset: make a new closure
my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())
print(my_closure())

# in summary
# global scope: shared by any function
# local scope: local to a particular function
# lexical scope: effectively global to an inner function returned
# if a value for a variable is not found in the immediate scope, 
# Python will look in the next scope level up (immediate parent) and so on
# ALL 3 may use the same variable name with no conflict
# but it's probably not a good idea to do this!