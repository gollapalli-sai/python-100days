def add(*args):
    print(args)

add(3,5,6)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3,multiply=5)