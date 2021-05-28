class Employee:
    def __init__(self,idno=0,name="name",sal=0.0):
        self.idno=idno
        self.name=name
        self.salary=sal


    def display(self):
        print("idno:",self.idno)
        print("name:",self.name)
        print("salary:",self.salary)

e1=Employee()
print("e1:")
e1.display()

e2=Employee(101)
print("e2:")
e2.display()

e3=Employee(102,"Ravi",125000.00)
print("e3:")
e3.display()

e4=Employee(name="Krishna")
print("e4:")
e4.display()

e5=Employee(sal=120000.00)
print("e5:")
e5.display()

e6=Employee(sal=450000.00,idno=105)
print("e6:")
e6.display()
