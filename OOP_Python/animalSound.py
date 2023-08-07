class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!!"
    
dog = Dog("Buddy")
cat = Cat("Whiskers")

animals = [dog , cat]

for animal in animals:
    print(animal.speak())