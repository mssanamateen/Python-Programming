numerator =int(input("enter the number1:"))
denominator = int(input("enter the number2:"))
try:
    result = numerator/denominator
except:
    print("Error: Denominator cannot be 0.")
else:
    print(result)

