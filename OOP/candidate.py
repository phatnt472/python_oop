from ngaythang import * 
from prettytable import *

class Candidate:
    id_can = 1
    def __init__(self,name='',date=Date(),math=0,liturature=0,english=0):
        
        self.name = name
        self.date = date
        self.math = math
        self.liturature = liturature
        self.english = english
        self.id = Candidate.id_can
        Candidate.id_can += 1
    def total_score(self):
        return self.math+self.liturature+self.english
    def __str__(self):
        return f'Id: {self.id}\nName: {self.name}\nDate of birth: {str(self.date)}\nScore: {self.total_score()}'

class TestCandidate(Candidate):
    def __init__(self,num_candidates, candidates):
        self.num_candidates = num_candidates
        self.candidates = candidates
    @classmethod
    def input(self):
        self.num_candidates = int(input("Enter number of candidate: "))
        self.candidates = []
        for i in range(self.num_candidates):
            name = input("Enter name: ")
            date = Date()
            date.input()
            math = None
            while 1:
                math= float(input("Enter math score: "))
                if 0 <= math<= 10:
                    break
            literature = None
            while 1:
                literature= float(input("Enter literature score: "))
                if 0 <= literature<= 10:
                    break
            english = None
            while 1:
                english = float(input("Enter english score: "))
                if 0 <= english<= 10:
                    break
            candidate = Candidate(name,date,math,literature,english)
            self.candidates.append(candidate)

            
    @classmethod
    def score_great15(self):
        table = PrettyTable()
        table.field_names = ['Id', 'Name', 'Date of Birth', 'Total Score']
        for candidate in self.candidates:
            if candidate.total_score() > 15:
                table.add_row([candidate.id, candidate.name, candidate.date,candidate.total_score()])
        print(table)

TestCandidate.input()
TestCandidate.score_great15()
