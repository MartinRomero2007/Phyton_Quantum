mensaje = """
1) Cuadrado
2) Rectángulo
"""

print(mensaje)
opcion = int(input('Ingrese el tipo de figura: '))
if opcion == 1:
    lado = int(input(f'Ingrese el lado del cuadrado: '))
    area = lado * lado
    print(f'El lado del cuadrado es: {area}')
elif opcion == 2:
    lado1 = int(input(f'Ingrese el primer lado del rectángulo: '))
    lado2 = int(input(f'Ingrese el segundo lado del rectángulo: '))
    per = (lado1 * 2) + (lado2 * 2)
    print(f'El perímetro del rectángulo es: {per}')
else:
    print('La opción ingresada no es válida')