from collections.abc import MutableSequence # Abstract Bases Classes

class ListaMutavel(MutableSequence): # Classe que herda de uma ABC
    pass

objetoValidado = ListaMutavel() # Erro devido à falta dos métodos obrigatórios
print(objetoValidado)
