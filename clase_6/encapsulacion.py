class Coordenada():
    def __init__(self, x=0 , y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, coor_x):
        if coor_x < 0:
            raise ValueError('No es una coordenada válida para X')
        else:
            self.__x = coor_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, coor_y):
        if coor_y < 0:
            raise ValueError('No es una coordenada válida para Y')
        else:
            self.__y = coor_y

    def distance(self, coor):
        if isinstance(coor, Coordenada):
            res_x = (self.__x + coor.x)**2
            res_y = (self.__y + coor.y)**2
            resultado = (res_x + res_y)**1/2
            return resultado
            
        raise ValueError('No es una coordenada válida.')

coord_1 = Coordenada()
coord_1.x = 100
coord_1.y = 2
print(coord_1.x)
print(coord_1.y)


coord_2 = Coordenada()
coord_2.x = 50
coord_2.y = 10
print(coord_2.x)
print(coord_2.y)
print(coord_1.distance(coord_2)) 