class Date:
    day = 1
    month = 1
    year = 1
    def __init__(self,day=1,month=1,year=1):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def __str__(cls):
        d = cls.day if  cls.day >= 10 else '0' + str(cls.day)
        m = cls.month if cls.month >= 10 else '0' + str(cls.month)
        y = cls.year
        return f'{d}/{m}/{y}'
    @classmethod
    def  check_leap_year(cls):
        return (cls.year % 100 != 0 and  cls.year % 4 == 0 ) or  cls.year % 400 == 0
    
    @classmethod
    def check_date(cls):
        day_of_month = cls.get_day_of_month() 
        if (0 < cls.day <= day_of_month) and  (1 <= cls.month <= 12)  and  (1 <= cls.year <= 10000):
            return True
        return False
        

    @classmethod
    def input(cls):
        date = input("Enter a day have format dd/mm/yyyy: ")
        lst = map(int,date.split('/'))
        cls.day,cls.month,cls.year = [i for i in lst]
        while cls.check_date() == False:
            date = input("Enter a day have format dd/mm/yyyy: ")
            lst = map(int,date.split('/'))
            cls.day,cls.month,cls.year = [i for i in lst]
        
    @classmethod
    def get_day_of_month(cls):
        day_of_month =  None
        if cls.month in [4,6,9,11]:
            day_of_month = 30
        elif cls.month in [1,3,5,7,8,10,12]:
            day_of_month = 31
        if cls.check_leap_year() == True:
            if cls.month == 2:
                day_of_month = 29
        else:
            if cls.month == 2:
                 day_of_month = 28
        return day_of_month
        
    @classmethod
    def get_the_next_day(cls):
        day_of_month = cls.get_day_of_month()
        if cls.day < day_of_month:
            cls.day += 1
        elif cls.day == day_of_month:
            cls.day = 1
            if  0 <cls.month < 12:
                cls.month += 1
            elif cls.month == 12:
                cls.month = 1
                cls.year += 1
        d = cls.day if  cls.day >= 10 else '0' + str(cls.day)
        m = cls.month if cls.month >= 10 else '0' + str(cls.month)
        y = cls.year
        print(f'{d}/{m}/{y}')
    
