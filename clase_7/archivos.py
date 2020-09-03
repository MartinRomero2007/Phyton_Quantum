import os 
#Imprimir nombres de los archivos en una lista de una determinada ruta
listado = os.listdir('C:\Users\FAM. ROMERO SIGUAS\Downloads')
for i in listado:
    print(i)


#Lista los archivos a manera de objeto DirEntry
escaneo = os.scandir('')
with escaneo as entries:
    for escaneo in entries:
        print(entry.path) #muestra ruta de una direccion de archivos, si usamos name muestra nombres
    
#print(escaneo)

#Enlistar directorios
listado = os.listdir('C:\Users\FAM. ROMERO SIGUAS\Downloads')
for i in listado:
    if os.path.isdir(os.path.join('C:\Users\FAM. ROMERO SIGUAS\Downloads', i)):
        print(i)


try:
    os.mkdir('C:\Users\FAM. ROMERO SIGUAS\Downloads\carpeta_nueva')
except FileExistsError:
    print('El directorio ya existe')

try:
    os.rename('C:\Users\FAM. ROMERO SIGUAS\Downloads\carpeta_nueva', 'C:\Users\FAM. ROMERO SIGUAS\Downloads\carpeta_nueva2')
except:
    print('Hubo un error.')

#Hace lo mismo que pwd (consola) que es mostrarnos la ruta
print(os.getcwd())