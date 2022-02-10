

from math import e


class phanso:

    def __init__(self,tu_so=0,mau_so=1):
        self.tu_so = tu_so
        self.mau_so=mau_so

    def nhap(self):
        tu = int(input("Nhập tử số: "))
        self.tu_so = tu
        mau = None
        while 1:
            mau=int(input("Nhập mẫu số: "))
            if mau != 0:
                break
        self.mau_so = mau

    def xuat(self):
        if self.mau_so != 1:
            print(f'{self.tu_so}/{self.mau_so}')
        else:
            print(f'{self.tu_so}')

    def rut_gon(self):
        u = ucln(self.tu_so, self.mau_so)
        self.tu_so //= u
        self.mau_so //= u
        if self.mau_so < 0:
            self.tu_so*=-1
            self.mau_so*=-1

    def __str__(self):
        return f'{self.tu_so}/{self.mau_so}' if self.mau_so  != 1 else  f'{self.tu_so}'
        
    def __repr__(self):
        return f'Tử số: {self.tu_so}\nMẫu số: {self.mau_so}'
    
    def __add__(self, other):
        temp = phanso()
        temp.tu_so = self.tu_so*other.mau_so +self.mau_so* other.tu_so
        temp.mau_so = self.mau_so*other.mau_so
        temp.rut_gon()
        return temp
   
    def __sub__(self,other):
        temp = phanso()
        temp.tu_so = self.tu_so*other.mau_so - self.mau_so* other.tu_so
        temp.mau_so = self.mau_so*other.mau_so
        temp.rut_gon()
        return temp   
    
    def __mul__(self, other):
        temp = phanso()
        temp.tu_so = self.tu_so*other.tu_so
        temp.mau_so = self.mau_so*other.mau_so
        temp.rut_gon()
        return temp   

    def __truediv__(self, other):
        temp  = phanso()
        if other.tu_so != 0:
            temp.tu_so = self.tu_so*other.mau_so
            temp.mau_so = self.mau_so*other.tu_so
            temp.rut_gon()
        return temp

    def __gt__(self, other):
        return self.tu_so/self.mau_so > other.tu_so/self.mau_so
    
    def __ge__(self, other):
        return self.tu_so/self.mau_so >= other.tu_so/self.mau_so
   
    def __lt__(self, other):
        return self.tu_so/self.mau_so < other.tu_so/self.mau_so
    
    def __le__(self, other):
        return self.tu_so/self.mau_so <= other.tu_so/self.mau_so
    
    def __eq__(self, other):
        return self.tu_so == other.tu_so and self.mau_so == other.mau_so
    
    def __ne__(self, other):
        return self.tu_so != other.tu_so and self.mau_so != other.mau_so

    def get_mau_so(self):
        return self.mau_so
    
    def get_tu_so(self):
        return self.tu_so
    
    def set_tu_so(self, value):
        self.tu_so = value
    
    def set_mau_so(self, value):
        self.mau_so = value

def  ucln(a,b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return 1
    else:
        while a != b:
            if a > b : 
                a -= b
            else:
                b -= a
    return a

def main():
    ps = phanso()
    ps.nhap()
    ps.rut_gon
    ps.xuat()
    print("+"*20)
    ps1 = phanso()
    ps1.nhap()
    ps1.rut_gon()
    ps2 = phanso()
    ps2.nhap()
    ps2.rut_gon()
    print(f'{ps1} + {ps2} = {ps1+ps2}')
    print(f'{ps1} - {ps2} = {ps1-ps2}')
    print(f'{ps1} * {ps2} = {ps1*ps2}')
    if ps2.get_tu_so() == 0: 
        print("Không thể thực hiện phép toán này!")
    else:
        print(f'{ps1} / {ps2} = {ps1/ps2}')
    if ps1 > ps2:
        print(f'Max: {ps1}')
    else:
        print(f'Max: {ps2}')



if __name__ == '__main__':
    main()