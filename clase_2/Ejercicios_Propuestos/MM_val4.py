def valor1_mayor():
    print(f'El valor {valor1} es el mayor ingresado')
    if valor2 < valor3 and valor2 < valor4:
        print(f'El valor {valor2} es el menor ingresado')
    elif valor3 < valor2 and valor3 < valor4:
        print(f'El valor {valor3} es el menor ingresado')
    elif valor4 < valor2 and valor4 < valor3:
        print(f'El valor {valor4} es el menor ingresado')

def valor2_mayor():
    print(f'El valor {valor2} es el mayor ingresado')
    if valor1 < valor3 and valor1 < valor4:
        print(f'El valor {valor1} es el menor ingresado ')
    elif valor3 < valor1 and valor3 < valor4:
        print(f'El valor {valor3} es el menor ingresado')
    elif valor4 < valor1 and valor4 < valor3:
        print(f'El valor {valor4} es el menor ingresado')

def valor3_mayor():
    print(f'El valor {valor3} es el mayor ingresado')
    if valor1 < valor2 and valor1 < valor4:
        print(f'El valor {valor1} es el menor ingresado ')
    elif valor2 < valor1 and valor2 < valor4:
        print(f'El valor {valor2} es el menor ingresado')
    elif valor4 < valor1 and valor4 < valor2:
        print(f'El valor {valor4} es el menor ingresado')

def valor4_mayor():
    print(f'El valor {valor4} es el mayor ingresado')
    if valor1 < valor2 and valor1 < valor3:
        print(f'El valor {valor1} es el menor ingresado')
    elif valor2 < valor1 and valor2 < valor3:
        print(f'El valor {valor2} es el menor ingresado')
    elif valor3 < valor1 and valor3 < valor2:
        print(f'El valor {valor3} es el menor ingresado')

valor1 = float(input(f'Ingrese un primer valor: '))
valor2 = float(input(f'Ingrese un segundo valor: '))
valor3 = float(input(f'Ingrese un tercer valor: ')) 
valor4 = float(input(f'Ingrese un cuarto valor: '))

if valor1 > valor2 and valor1 > valor3 and valor1 > valor4:
    valor1_mayor()
elif valor2 > valor1 and valor2 > valor3 and valor2 > valor4:
    valor2_mayor()
elif valor3 > valor1 and valor3 > valor2 and valor3 > valor4:
    valor3_mayor()
elif valor4 > valor1 and valor4 > valor2 and valor4 > valor3:
    valor4_mayor()
else:
    print(f'Error: Algunos valores ingresados son idénticos') 