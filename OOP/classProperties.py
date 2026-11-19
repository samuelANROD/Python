#validação antes de permitir que alguém modifique um atributo
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("não pode ser negativo")

        self._price = value

product = Product(1000)

product.price = 1000

print(product.price)