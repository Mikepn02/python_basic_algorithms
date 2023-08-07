from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year,self.date_of_birth.month, self.date_of_birth.day):
            age-=1
        return age

# Example usage

year = int(input("Enter current year of your birth: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
names=input("Enter your names: ")
country = input("Enter you country: ")

person = Person(names, country, date(year, month, day))


print("Person 1:")
print("Name:", person.name)
print("Country:", person.country)
print("Date of Birth:", person.date_of_birth)
print("Age:", person.calculate_age())

