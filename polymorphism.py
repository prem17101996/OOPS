class parrot():
    def fly(self):
        print("Parrot Can Fly")

    def swim(self):
        print("Parrot Can Not Swim ")
class penguin():
    def fly(self):
        print("Penguin Can not Fly")

    def swim(self):
        print("Penguin Can Swim ")
def flytest(bird):
    bird.fly()

catobj=parrot()
dogobj=penguin()
flytest(catobj)
flytest(dogobj)
