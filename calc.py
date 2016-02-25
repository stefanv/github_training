def add(a, b):
    return a + b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("You should not try to divide by zero!")
