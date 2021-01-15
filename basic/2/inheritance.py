class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print(f'{self.name} is being annoying')


dog1 = Dog("Ben")
dog1.walk()
dog1.bark()

cat1 = Cat("Kitty")
print(cat1.name)
cat1.be_annoying()
