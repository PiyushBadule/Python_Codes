class Employee:
    def __init__(self, id_no=0, name="name", salary=0.0):
        """
        Initialize an Employee object with id number, name, and salary.

        Parameters:
        id_no (int): Employee's ID number. Defaults to 0.
        name (str): Employee's name. Defaults to 'name'.
        salary (float): Employee's salary. Defaults to 0.0.
        """
        self.id_no = id_no
        self.name = name
        self.salary = salary

    def display(self):
        """
        Display the details of the Employee.
        """
        print("ID Number:", self.id_no)
        print("Name:", self.name)
        print("Salary:", self.salary)

def main():
    """
    Main function to demonstrate the functionality of the Employee class.
    """
    e1 = Employee()
    print("e1:")
    e1.display()

    e2 = Employee(101)
    print("e2:")
    e2.display()

    e3 = Employee(102, "Ravi", 125000.00)
    print("e3:")
    e3.display()

    e4 = Employee(name="Krishna")
    print("e4:")
    e4.display()

    e5 = Employee(salary=120000.00)
    print("e5:")
    e5.display()

    e6 = Employee(salary=450000.00, id_no=105)
    print("e6:")
    e6.display()

if __name__ == "__main__":
    main()
