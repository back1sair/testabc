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

def modulo(a: float, b: float) -> float:
    """
    Calculate the remainder of a divided by b.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The remainder of a divided by b

    Raises:
        ValueError: If b is 0
    """
    if b == 0:
        raise ValueError("Division by zero: b cannot be 0")
    return a % b

print("hello world")
