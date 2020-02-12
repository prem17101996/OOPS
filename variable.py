
# CLASS VARIABLE AND INSTANCE VARIABLE


class student:
    clg="knit" #class variable
    def __init__(self,name,roll):
        self.name=name #instance variable
        self.roll=roll
    def display(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("clg name:",student.clg)

obj=student("prem","188607")
obj.display()
