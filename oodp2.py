"""Q1. Student Class (Basic)
Create a class Student with attributes: name, age, mark.

Write a method display() to print all details."""
class student():
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
    def display(self):
        print(self.name, self.age, self.mark)
c1= student("John", 22, "M")
c1.display()