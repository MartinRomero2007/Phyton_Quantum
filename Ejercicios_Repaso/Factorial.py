# Calcular el factorial de un número
def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact *= i 
        #que es lo mismo que fact = fact * i
    return fact

numero = int(input('Ingresa un número: '))
print(factorial(numero))