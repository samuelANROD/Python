#funções são basicamente um agrupado de instruções que executam tarefas
#elas são importantes para evitar repetição
def hello_func():

#esse pass serve só para mostrar que talvez essa função seja usada
    pass

#assim você imprime a função em si
print(hello_func)
print(hello_func())
#--------------------------------------------------------------------
#como atribuir valor a função
def ola():
    print("hello world")

ola()
#--------------------------------------------------------------------
def ola_print():
    print("hello world")

def ola_return():
    return "hello world"

ola_print()     # aparece "hello world" na tela
ola_return()    # não aparece nada!

#---------------------------------------------------------------------
#como usar return colocando o parametro dentro da função
#parametro pode ter qualquer nome
def hello(greeting):
    return f'{greeting} function '
print(hello("hi"))

def name_age(name, age):
    return f'my name is {name} and i am {age} years old'
print(name_age(name = 'sam', age = 20))


