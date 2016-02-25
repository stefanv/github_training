def multiply(a, b=None):
    """Multiply two numbers.

    Parameters
    ----------
    a : int or float 
        First operand.
    b : int or float (optional)
        Second operand.
    Returns
    -------
    output : int or float
        Multiplication of parameters, or a*a if b not provided. 
    """
    return a * a if b is None else a * b
