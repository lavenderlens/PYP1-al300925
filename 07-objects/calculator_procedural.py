# procedural module contains just functions, one global variable to keepa. running total, and a runtime
# calculator with four arithmetic functions and a function to return the running total and reset it

total = 0

def add(num):
    global total
    total += num
# add(2)
# print(total)#expect: 2

def sub(num):
    global total
    total -= num

def mul(num):
    global total
    total *= num

def div(num):
    global total
    if num != 0:
        total /= num

def equals():
    global total
    temp_total = total
    total = 0
    return temp_total

if __name__ == "__main__":
    add(5)
    sub(2)
    mul(3)
    div(9)
    #expected 1.0
    print(equals())#1.0
    
