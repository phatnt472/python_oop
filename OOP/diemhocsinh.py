from prettytable import *
class Student:
    def __init__(self,name="Phát", math_score = 10.0, literature_score = 10.0):
        self.name = name
        self.math_score = math_score
        self.literature_score = literature_score

    def get_name(self):
        return self.name
    def get_math_score(self):
        return self.math_score
    def get_literature_score(self):
        return self.literature_score
    
    @property
    def get_avg_score(self):
        return (self.math_score + self.literature_score)/2

    @staticmethod
    def input(arr,num):
        for i in range(num):
            name = input("Nhập tên học sinh: ")
            math_score = None
            while 1:
                math_score = float(input("Nhập điểm toán: "))
                if 0 <= math_score <= 10:
                    break
            while 1:
                literature_score = float(input("Nhập điểm văn: "))
                if 0 <= literature_score <= 10:
                    break
            temp =  Student()
            temp.name = name
            temp.literature_score =literature_score
            temp.math_score = math_score
            arr.append(temp)


            
    @staticmethod
    def output(arr):
        x = PrettyTable()
        x.field_names = ["Họ và tên","Điểm toán","Điểm văn","Điểm trung bình"]
        for item in arr:
          x.add_row([item.get_name(), item.get_math_score(), item.get_literature_score(), item.get_avg_score])
        print(x)

num = int(input("Nhập số học sinh: "))
arr = []
Student.input(arr,num)

Student.output(arr)