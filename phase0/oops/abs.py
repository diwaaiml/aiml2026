from abc import ABC, abstractmethod

class AbsClass(ABC):
    @abstractmethod
    def Name(self,name):
        pass
    @abstractmethod
    def Name(self,place):
        pass

class TeacherClass(AbsClass):
    def Name(self,name):
        print("Hi this is "+name)
    def Profession(self,place):
        print("I am a teacher from "+place)

class StudentClass(AbsClass):
    def Name(self,name):
        print("Hi this is "+name)
    def Profession(self,place):
        print("I am a student from "+place)

class MainClass:
    def __init__(self,className):
        self.className=className
    
    def callThem(self,name,place):
        self.className.Name(name)
        self.className.Profession(place)
        print("------Next------")

sC = StudentClass()
mc = MainClass(sC)
mc.callThem("Diwa","trichy")

tC = TeacherClass()
mc2 = MainClass(tC)
mc2.callThem("Raji","trichy")


