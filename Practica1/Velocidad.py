def velocidad(km):
    cms = round(km * 27.7 , 0)
    print(f'La velocidad en cm/s es: {cms}')

vel = float(input('Ingrese la velocidad en km/h: '))
velocidad(vel)
