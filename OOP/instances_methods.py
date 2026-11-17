#metodos que pertencem às instâncias

#Instance Methods são métodos que permitem que um objeto execute ações utilizando seus próprios atributos.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount

    def show_balance(self):
            print(f"owner: {self.owner}")
            print(f"balance: R${self.balance}")

    def withdraw(self, amount):
        if self.balance >=  amount:
            self.balance -= amount
        else :
            print("insufficient balance")

account = BankAccount("samuel", 100)

account.deposit(50)
account.show_balance()
account.withdraw(50)