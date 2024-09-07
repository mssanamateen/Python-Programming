num=int(input("enter the value for the number:"))

if num<0:
	print("negative numbers not allowed")
elif num==0:
	print("number should be greater than zero")
else:
	print("select the operation")
	print("1.factorial of a number")
	print("2.Armstrong number")
	ch=int(input("enter ur choice"))
	if ch==1:
		fact=1
		for i in range(1,num+1):
			fact=fact*i
		print(f"factorial of {num} is",fact)
	elif ch==2:
		sum=0
		temp=num
		while temp>0:
			digit=temp%10
			sum+=digit**3
			temp//=10
		if sum==num:
			print("armstrong number")
		else:
			print("not an armstrong number")
	else:
		print("Give correct choice")