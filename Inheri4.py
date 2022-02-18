class Child:

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is student
    def isStudent(self):
        return False

# Derived class or Child class
class Student(Child):

    # True is returned
    def isStudent(self):
        return True


# Driver code
# An Object of Child
std = Child("Akshada")
print(std.getName(), std.isStudent())

# An Object of Student
std = Student("Swapnali")
print(std.getName(), std.isStudent())