"""Create a class hierarchy: Person → Employee → Manager. Add methods in each and print details."""
class person():
    def __init__(self,name,dob,fname,mname):
        self.name = name
        self.dob = dob
        self.fname = fname
        self.mname = mname
class employee(person):
    def __init__(self,empname,salary):
        self.empname = empname
        self.salary = salary
class manager(employee):
    def __init__(self):
        print("this is a manager constructor")
    def display(self):
        print(self.name)
        print(self.dob)
        print(self.empname)
        print(self.salary)
m = manager("prithivraj",25000)
m.display()
        

