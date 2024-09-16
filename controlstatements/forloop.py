#prime numbers 
num=int(input("enter the number:"))

if num>1:

	for i in range(2,(num//2)+1):
		if num%i ==0:
			print("not a prime")
			break
	else:
		print("number is prime")
else:
	print("not a prime")