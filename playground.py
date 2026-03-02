'''
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

is the same as 


def fun(a, b, c):
    return a + b + c

print(fun(5, 10, 15))

is the same as 

def fun(a, b, c):
    return sum([a, b, c])

print(fun(5, 10, 15))

set: {a, b, c}

dict: {a: 1, b: 2, c: 3}

tuple: (a, b, c)

list: [a, b, c]

'''

def fun(a, b, c):
    return sum((a, b, c))

print(fun(5, 10, 15))
