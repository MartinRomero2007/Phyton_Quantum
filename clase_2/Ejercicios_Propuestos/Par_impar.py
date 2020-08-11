def par():
    print(f'El número {numero} que ha ingresado es par')

numero = int(input(f'Ingrese un número: '))
par = int(numero/2)

if numero == par :
    par()
else:
    print(f'El número {numero} que ha ingresado es impar')