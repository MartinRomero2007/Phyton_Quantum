contador = 0
with open('aleph.txt') as f:
    for linea in f:
        contador += linea.count('Beatriz')

print(f'Beatriz se encuentra {contador} veces en el texto.')