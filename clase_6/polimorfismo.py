class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} está avanzando.')

    def saluda(self):
        print(f'{self.nombre} está saludando.')

class Ciclista():
    def __init__(self, nombre):
        super().__init__(nombre) 
    
    def avanza(self):
        print(f'El ciclista {self.nombre} está avanzando en su bicicleta.')

persona_1 = Persona('Martin')
persona_1.avanza()
persona_1.saluda()

persona_2 = Persona('Jarmila')
persona_2.avanza()
persona_2.saluda()