class function:
    def __init__(self,a,b):
        self.c=a+b
class add(function):
    def display(self):
        print(self.c)

obj=add(int(input("enter a:")),(int(input("enter b:"))))

obj.display()