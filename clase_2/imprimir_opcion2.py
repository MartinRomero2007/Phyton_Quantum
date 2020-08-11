def imprimir_mensaje(opcion):
    print('Hola: ')
    print('Cómo estás?')
    print(f'Elegiste la opción {opcion}')
    print('Adiós')

opcion = input('Ingresa una opción: ')
if opcion == '1':
    imprimir_mensaje(opcion)   
elif opcion == '2':
    imprimir_mensaje(opcion)
elif opcion == '3':
    imprimir_mensaje(opcion)
elif opcion == '4':
    imprimir_mensaje(opcion)
else:
    print('La opción elegida es incorrecta')