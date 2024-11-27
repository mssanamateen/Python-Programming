try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):  
    print("An error occurred: ValueError or ZeroDivisionError")
else:
    print(f"Result is: {result}")
