def mayor_menor():
    print(f'El valor {valor1} es el mayor ingresado')
def menor_mayor():
    print(f'El valor {valor2} es el mayor ingresado')

valor1 = float(input(f'Ingrese un primer valor: '))
valor2 = float(input(f'Ingrese un segundo valor: '))

if valor1 > valor2:
    mayor_menor()
elif valor1 < valor2:
    menor_mayor()
else:
    print(f'Ambos valores ingresados son idénticos') 