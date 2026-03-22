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

def factorial(n: int) -> int:
    """
    Calculate the factorial of n.

    Args:
        n: The non-negative integer

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """
    Check whether n is a prime number.

    Args:
        n: The integer to check

    Returns:
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print("hello world")
