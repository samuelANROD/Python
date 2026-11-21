#serve basicamente como proteção de dados
#para impedir que qualquer pessoa altere o dado
class BankAccount:
    #encapsulation:
    #_atributo : deve ser tratado como interno
    #__atributo : privados
    #atributo : publico
    #@property : para controle

    def __init__(self, owner, balance):
        self.owner = owner # publico
        self.__balance = balance # privado

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("O valor precisa ser maior que zero")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("O valor precisa ser maior que zero")

        if amount > self.__balance:
            raise ValueError("Saldo insuficiente")

        self.__balance -= amount

    def show_balance(self):
        return self.__balance


account = BankAccount("Samuel", 1000)

account.deposit(500)
account.withdraw(200)

print(account.owner)
print(account.show_balance())

#caso com property

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("O valor precisa ser maior que zero")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("O valor precisa ser maior que zero")

        if amount > self.__balance:
            raise ValueError("Saldo insuficiente")

        self.__balance -= amount


account = BankAccount("Samuel", 1000)

account.deposit(500)
account.withdraw(200)

print(account.owner)
print(account.balance)