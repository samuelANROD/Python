#classes permitem agrupar dados e funções de maneira facil e reutilizavel
#exemplo de classe:


class Employee:
#função para atribuir de uma forma genérica cada uma desses dados
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@" + "gmail.com"
#função para juntar os nomes
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

employees = []

for i in range(2):
    first = input(f'employee {i + 1} First name: ')
    last = input(f'employee {i + 1} Last name: ')
    pay = int(input(f'employee {i + 1} Salary: '))

    emp = Employee(first, last, pay)
    employees.append(emp)

for emp in employees:
    print(emp.first)
    print(emp.last)
    print(emp.pay)
    print(emp.email)
    print(emp.fullname())
    print(" ")