def imprimir_impares():
    for i in range(101):
        if i % 2 != 0:
            contador += 1
            print(i)
    print('El número de impares es: {contador}')

imprimir_impares()