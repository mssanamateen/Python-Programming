#fibonacci series
'''The Fibonacci series is a sequence of numbers in which each number is 
the sum of the two preceding ones, often beginning with 0 and 1.'''

num=int(input("enter the limit:"))

x,y=0,1
print(x,y,end=' ')

i=0
#while loop runs for num-2 times as  the first two digits are defined already
while(i<num-2):
	z=x+y
	print(z,end=' ')
	x=y
	y=z
	i=i+1