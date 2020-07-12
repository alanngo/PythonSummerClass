# __init__ initalizes the instance variables
# self: refering to Student's class

class Student:
    def __init__(self, exam1, exam2, exam3):
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3

    def calc_avg(self):
        return (self.exam1 + self.exam2 + self.exam3) / 3
