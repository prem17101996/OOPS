class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class student2(student):
    def display(self):
        print("name-",self.name)
        print("rollno-",self.rollno)
obj=student2(input("enter name:"),(int(input("enter rollno:"))))
