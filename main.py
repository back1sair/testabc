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

def divide(a: float, b: float) -> float:
    """
    Divide two numbers and return the result.

    Args:
        a: The dividend (number to be divided)
        b: The divisor (number to divide by)

    Returns:
        The quotient of a divided by b

    Raises:
        ValueError: If b is 0 (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("hello world")
