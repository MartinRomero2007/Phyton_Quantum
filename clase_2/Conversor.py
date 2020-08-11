mensaje = """
Hola, este es un conversor de monedas
Ingresa cualquiera de estas 3 opciones:
1. Soles - Dólares
2. Euros - Dólares
3. Pesos Colombianos - Dólares
"""
print(mensaje)
opcion = int(input('Ingresa la opción: '))
if opcion == 1:
    tipo_de_cambio = 0.28
    monto = float(input('Hola, ingresa tu monto en soles: '))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dólares es: {monto_dolares}')
elif opcion == 2:
    tipo_de_cambio = 1.19
    monto = float(input('Hola, ingresa tu monto en euros: '))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dólares es: {monto_dolares}')
elif opcion == 3:
    tipo_de_cambio = 0.00027
    monto = float(input('Hola, ingresa tu monto en pesos colombianos: '))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dólares es: {monto_dolares}')