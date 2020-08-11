def imprimir_mensaje(opcion):
    print(
        f"""
        Hola
        Cómo estás?
        Elegiste la opción {opcion}
        Adiós
    """
    )
opcion = input('Ingrese la opción: ')
if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
    imprimir_mensaje(opcion)
else:
    print('Opción Incorrecta: ')