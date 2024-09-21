class student:
    def __init__(self,nm='.',age=15,m=0):
        self.name=nm
        self.age=age
        self.marks=m
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("marks:",self.marks)

s = student("kushal",21,61)
s.display()
s1 = student("abhishek")
s1.display()