def suma_pares_impares():
    suma_pares = 0
    suma_impares = 0
    for i in range(101):
        print(i)
        if i % 2 == 0:
            suma_pares += 1
        else:
            suma_impares += 1
    print(f'La suma de pares es: {suma_pares}')
    print(f'La suma de impares es: {suma_impares}')

suma_pares_impares()
