#eles não recebem nenhum valor cls ou self
#são apenas funções comuns dentro de classe
#seu uso se resume em deixar código organizado DRY
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 1.8) + 32

resultado = Temperature.celsius_to_fahrenheit(30)
print(resultado)