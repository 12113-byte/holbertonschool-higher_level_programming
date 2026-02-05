#!/usr/bin/python3
import sys

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Hello Jonathan, my name is {self.name}.")

    def __str__(self):
        return f"You got me: {self.name}, {hex(id(self))}."

    def __del__(self):
        print(f"{self.name} is leaving the class.")

    def __add__(student1, student2):
        return Student(student1.name + student2.name)

    #getter
    @property
    def name(self):
        #print("Get the name.")
        return(self.__name)
    
    #setter
    @name.setter
    def name(self, new_name):
        #print("Set the name.")
        self.__name = new_name.capitalize()

class C28(Student):
    def __init__(self, name):
        super().__init__(name)
        print("We are very noisy.")

def main():
    #print("Hello World!")
    #matt = Student("matt")
    #print(matt)
    #print(f"{hex(id(matt))}")
    #lachie = Student("Lachie")
    #print(f"{hex(id(lachie))}")
    #s = matt + lachie
    #print(s)
    s = Student("sebastian")
    uliana = C28("uliana")

    #anon = matt
    #print(f"{hex(id(anon))}")

    #print(sys.getrefcount(matt))
    #print(sys.getrefcount(lachie))
    #print(sys.getrefcount(anon))

    #lachie.__name = "golden legs"
    #print(f"{lachie.__name}")

if __name__ == "__main__":
    main()
