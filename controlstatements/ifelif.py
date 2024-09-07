a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
print("select the operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus operation")
choice=input("enter ur choice:")

if choice=='1':
	print(f"{a}+{b} =",(a+b))
elif choice=='2':
	print(f"{a}-{b} =",(a-b))
elif choice=='3':
	print(f"{a}*{b} =",(a*b))
elif choice=='4':
	print(f"{a}/{b} =",(a/b))
elif choice=='5':
	print(f"{a}%{b} =",(a%b))
else:
	print("select the correct choice")



