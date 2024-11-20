class Arithmetic:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def add(self):
        print(f"{self.n1}+{self.n2} is ={self.n1+self.n2}")
    def sub(self):
        print(f"{self.n1}-{self.n2} is ={self.n1-self.n2}")
    def mul(self):
        print(f"{self.n1}*{self.n2} is ={self.n1*self.n2}")
    def div(self):
        print(f"{self.n1}/{self.n2} is ={self.n1/self.n2}")


a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))

arith=Arithmetic(a,b)

arith.add()
arith.sub()
arith.mul()
arith.div()
