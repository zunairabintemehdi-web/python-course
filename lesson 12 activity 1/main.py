class Cat :
    def __init__(self,name,age):
        self.name= name
        self.age= age
    
    def info(self):
        print(f"It is a cat.Her name is{self.name}.It is {self.age} years old")

    def make_sound(self):
        print("meow")


class Dog :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Its a dog, its name is {self.name} , it is {self.age} years old ")

    def make_sound(self):
        print("Woof woof")

cat1= Cat("mimi",2)
dog1= Dog("bobo",7)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()