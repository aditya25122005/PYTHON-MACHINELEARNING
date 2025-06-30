class person:
    def __init__(self,name='xyz',age=-1):
        self.name=name
        self.age=age
    def introduce(s):
        print(f"Hi I am {s.name} My age is {s.age}")   
class Student(person):
    pass
             

s1=Student('Aditya',20)
s1.introduce()             