class Student:
    def __init__(self, name,id,faculty,avg_score):
        self.name = name
        self.id = id
        self.faculty =faculty
        self.avg_score = avg_score
    
class Regular_Student(Student):
    def __init__(self,name,id,faculty,avg_score,train_point):
        self.name = name
        self.id = id
        self.faculty = faculty
        self.avg_score = avg_score
        self.train_point = train_point

    @property
    def scholarship(self):
        qualified = False
        if self.train_point >= 85:
            qualified = True 
        scholarship = 0
        if qualified == True:
            if 7 <= self.avg_score < 8.5:
                scholarship = 1000000
            elif 8.5 <= self.avg_score < 9.5:
                scholarship = 1200000
            elif self.avg_score >= 9.5:
                scholarship = 1500000
        return scholarship

        



class Join_Student(Student):
    def __init__(self,name,id,faculty,avg_score,num_absence):
        self.name = name
        self.id = id
        self.faculty = faculty
        self.avg_score = avg_score
        self.num_absence = num_absence
    @property
    def scholarship(self):
        qualified = False
        if self.num_absence <= 3:
            qualified = True 
        scholarship = 0
        if qualified == True:
            if 7 <= self.avg_score < 8:
                scholarship = 1000000
            elif 8 <= self.avg_score < 9.5:
                scholarship = 1200000
            elif self.avg_score >= 9:
                scholarship = 1500000
        return scholarship


class