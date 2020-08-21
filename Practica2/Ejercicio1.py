def examen(q, e, r, s):
    clave_de_respuestas = [a, a, b, b]
    respuestas_est = []
    respuestas_est.append({q},{e}, {r}, {s})
    if clave_de_respuestas == respuestas_est:
        sumatoria == 20
        print(f'Tu puntaje es {sumatoria}')
    else:

        print('La respuesta elegida es incorrecta')




mensaje = """
    Hola bienvenido al sistema de examenes, eliga opciones de la A a la D"
"""
print(mensaje)
num1 = str(input(f' Ingrese su rpta. a la pregunta 1: '))
num2 = str(input(f' Ingrese su rpta. a la pregunta 2: '))
num3 = str(input(f' Ingrese su rpta. a la pregunta 3: '))
num4 = str(input(f' Ingrese su rpta. a la pregunta 4: '))
examen(num1, num2, num3, num4)
