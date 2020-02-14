class cat:
    def purr(self):
        print("meow")

class dog:
    def bark(self):
        print("bark")

class eat(cat,dog):
    def eat(self):
        print("eating")

obj=eat()
obj.eat()
obj.bark()
obj.purr()