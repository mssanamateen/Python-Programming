def check_positive(number):
    if number < 0:
        raise ValueError("The number must be positive!")
    return number

try:
    result = check_positive(-5)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
