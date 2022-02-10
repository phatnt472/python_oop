class Complex:
    def __init__(self,real=0,virtual=0):
        self.real = real
        self.virtual = virtual
    
    def  input(self):
        self.real = float(input("Enter real part: "))
        self.virtual = float(input("Enter virtual part: "))
    def output(self):
        print(f'{self.real} + {self.virtual}i')
    def __add__(self, other):
        if type(other) is int or type(other) is float:
            other= Complex(other)
        return  Complex(self.real + other.real,self.virtual+other.virtual)
 
    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            other= Complex(other)
        return  Complex(self.real -  other.real,self.virtual - other.virtual)
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            other= Complex(other)
        x = (self.real * other.real) - (self.virtual * other.virtual)
        y  =  (self.virtual * other.real) + (self.real * other.virtual)
        return Complex(x,y)
    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            other= Complex(other)
        x =  ((self.real * other.real) + (self.virtual * other.virtual)) / (other.real**2 + other.virtual**2)
        y  =  ((self.virtual * other.real) - (self.real * other.virtual)) / (other.real**2 + other.virtual**2)
        return Complex(x,y)
a = Complex(1,1)
a /= Complex(3,1)
a.output()



