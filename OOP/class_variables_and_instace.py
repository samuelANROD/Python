#classes de variavéis são aquelas que compartilham entre todas as instâncias de uma classe
class dates:
    # de uma forma simples
    # objetos podem ser diferentes
    # mas a class variable são universais
    species = "human"

    def __init__(self, name, year):
        #self é o próprio objeto
        #name e year parametros
        #e a junção vira um atributo

        #class instance
        self.name = name
        self.year = year

dates_list = []

for i in range(1):
    name = input("Name: ")
    year = int(input("Year: "))

    date = dates(name, year)
    dates_list.append(date)

for date in dates_list:
    print(f"name: {date.name}")
    print(f"name: {date.year}")

print(dates.species)

#__init__ methods serve basicamente para executar automaticamente
#supondo caso:
person = dates("samuel", 19)
#print(person.name)
#print(person.year)
#ele executa automaticamente o __init__ passando valores para name = "samuel" ...

#class variable x class instance
# v - universal e pertence a classe
# i - objetos e é atribuida compartilhada pela classe