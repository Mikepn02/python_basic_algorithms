class Student:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def getAge(self, age):
        self.age = age


student1 = Student("Hirwa", "Junior")
student1.getAge(40)
print(f"My last name is {student1.lastName} and My age is {student1.age}")

