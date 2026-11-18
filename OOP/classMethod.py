#exemplo simples de @classmethods
#ele basicamente permite que voce acesse ou modifique class variable
class Employee:
    company = "google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

me = Employee("samuel", 10000)
Employee.change_company("spaceX")

print("company: ", Employee.company)
print(me.name)
print(me.salary)