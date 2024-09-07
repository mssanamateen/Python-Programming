'''Square of given number '''
import math as mt
num=int(input("enter the number"))
if num!=0:
	res=mt.pow(num,2)
	print(f"{num}^2 is:",res)
else:
	print("give a number greater than 0")