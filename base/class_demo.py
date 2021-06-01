class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is sitting")


my_dog = Dog("li", 6)
my_dog.sit()


class Jinmao(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

my_jinmao = Jinmao("1a", 7)
my_jinmao.sit()