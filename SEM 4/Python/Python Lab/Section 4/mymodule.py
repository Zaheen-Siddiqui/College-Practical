# File: mymodule.py

def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
    except Exception as e:
        return f"Error in factorial: {e}"

def primeNumber(num):
    try:
        if not isinstance(num, int):
            raise ValueError("Input must be an integer.")
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    except Exception as e:
        return f"Error in primeNumber: {e}"

def powNumber(base, exponent):
    try:
        return base ** exponent
    except Exception as e:
        return f"Error in powNumber: {e}"
