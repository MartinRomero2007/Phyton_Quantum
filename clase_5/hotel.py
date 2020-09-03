class Hotel():
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def anadir_huespedes(self, cantidad_huespedes):
        self.huespedes += cantidad_huespedes

    def checkout(self, cantidad_huespedes):
        self.huespedes -= cantidad_huespedes

    def ocupacion_total(self):
        return self.huespedes 

hotel_chincha = Hotel(numero_maximo_de_huespedes=50 , lugares_de_estacionamiento= 20)
print(f'El número de huespedes es: {hotel_chincha.ocupacion_total}')
hotel_chincha.anadir_huespedes(50)
print(f'El número de huespedes es: {hotel_chincha.ocupacion_total}')
hotel_chincha.checkout(30)
print(f'El número de huespedes es: {hotel_chincha.ocupacion_total}')

#print(hotel_chincha.numero_maximo_de_huespedes)
#print(hotel_chincha.lugares_de_estacionamiento)