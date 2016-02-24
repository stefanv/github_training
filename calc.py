def add(a, b):
    return a + b

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("You should not try to divide by zero!")

def subtract(a, b):
    """
    Subtracts b from a.
    >>> subtract(4, 1)
    3
    >>> subtract(2, 3)
    -1
    """
    return a - b
