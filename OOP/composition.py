#uma classe utiliza objetos de outras classes como parte de sua estrutura.
# Classe independente
class Processor:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

    def show_info(self):
        print(f"Processor: {self.model}")
        print(f"Cores: {self.cores}")


# Outra classe independente
class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

    def show_info(self):
        print(f"RAM: {self.capacity} GB")


# Classe que utiliza os outros objetos
class Computer:
    def __init__(self, processor, ram):
        # O computador recebe objetos de outras classes
        self.processor = processor
        self.ram = ram

    def show_specs(self):
        print("Computer specifications:")

        # Chamando métodos dos objetos internos
        self.processor.show_info()
        self.ram.show_info()


# Criando os componentes
cpu = Processor("Intel i5", 6)
memory = RAM(16)

# Criando o computador com os componentes
computer = Computer(cpu, memory)

computer.show_specs()