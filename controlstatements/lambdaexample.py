greatA=lambda x,y,z: x>y and x>z
greatB=lambda x,y,z:y>x and y>z
greatC=lambda x,y,z:z>x and z>y

A=int(input("enter the value of A:"))
B=int(input("enter the value of B:"))
C=int(input("enter the value of C:"))
print(f"Is {A} greater?",greatA(A,B,C))
print(f"Is {B} greater?",greatB(A,B,C))
print(f"Is {C} greater?",greatC(A,B,C))