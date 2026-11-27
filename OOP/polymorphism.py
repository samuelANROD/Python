#logica simples basicamente pega o método do pai
#e tranforma ele assim ele passa a ter varias tipos

# Classe pai
class Animal:
    def make_sound(self):
        print("O animal faz um som.")

# Classe filha
class Dog(Animal):
    # Sobrescrevendo o método da classe pai
    def make_sound(self):
        print("Au au!")


class Cat(Animal):
    def make_sound(self):
        print("Miau!")


class Cow(Animal):
    def make_sound(self):
        print("Muuu!")


# Criando os objetos
dog = Dog()
cat = Cat()
cow = Cow()

# Mesmo método, comportamentos diferentes
dog.make_sound()
cat.make_sound()
cow.make_sound()