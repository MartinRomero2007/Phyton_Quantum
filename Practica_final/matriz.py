class Matriz():
    def __init__(self, tamano):
        self.tamano = tamano

    def crear_lista(self, matriz_lista):
        matriz_lista = []
        for i in matriz_lista:
            matriz_lista.append(tamano)
            self.tamano -= 1

        return matriz_lista

resultado = Matriz(tamano = 5)
print(f'El resultado es = {resultado}')