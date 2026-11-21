#Sua lógica é permitir que uma classe herde atributos e métodos de outra classe
# Classe pai (superclasse)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} está comendo.")

    def sleep(self):
        print(f"{self.name} está dormindo.")


# Classe filha (subclasse)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} está latindo.")


# Outra classe filha
class Cat(Animal):
    def meow(self):
        print(f"{self.name} está miando.")


# Criando objetos
dog = Dog("Jason", 3)
cat = Cat("Lucia", 2)

# Métodos herdados da classe Animal
dog.eat()
dog.sleep()

# Método próprio da classe Dog
dog.bark()

cat.eat()
cat.meow()

#exemplo de como puxar usando super()
#class Dog(Animal):
#    def __init__(self, name, breed):
#        super().__init__(name)  # Executa o __init__ da classe Animal
#       self.breed = breed      # Atributo exclusivo de Dog