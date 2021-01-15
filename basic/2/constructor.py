class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person('Peter')
person1.talk()

person2 = Person('Bob')
person2.talk()
