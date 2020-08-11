tipo_de_cambio = 0.28
monto_soles = input('Hola, ingresa tu monto en soles: ')
monto_soles = float(monto_soles)
monto_dolares = round(monto_soles * tipo_de_cambio, 2)
print(f'El monto en dólares es: {monto_dolares}')