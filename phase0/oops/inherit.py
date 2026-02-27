class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Bird(Dog):
    def bark2(self):
        print("Final")

d = Bird()
d.speak()
d.bark()