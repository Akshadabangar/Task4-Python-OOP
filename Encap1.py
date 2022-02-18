class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age

person = Person('Akshada', 20)
#accessing using class method
person.display()
#changing age using setter
person.setAge(25)
person.getAge()