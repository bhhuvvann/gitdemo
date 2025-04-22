"""This module provides a function to calculate the factorial of a non-negative integer."""

def factorial(n):
    """Calculate factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Negative numbers are not allowed.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    NUMBER = 5
    print(f"Factorial of {NUMBER} is {factorial(NUMBER)}")