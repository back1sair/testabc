def greet(name):
    return f"Hello, {name}!"

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the result.

    Args:
        a: The first number
        b: The second number

    Returns:
        The product of a and b
    """
    return a * b

def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers and return the result.

    Args:
        a: The first number
        b: The second number

    Returns:
        The difference of a and b
    """
    return a - b

def power(base: float, exp: float) -> float:
    """
    Raise base to the power of exp and return the result.

    Args:
        base: The base number
        exp: The exponent

    Returns:
        base raised to the power of exp
    """
    return base ** exp

print("hello world")
