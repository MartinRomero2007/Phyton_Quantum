def calcular_nota(resp_correctas , resp_alumno):
    nota_final = 0
    if resp_correctas[0] == resp_alumno[0]:
        nota_final += 4
    elif resp_alumno[0] == "":
        nota_final += 0
    else:
        nota_final -= 1
    
    if resp_correctas[1] == resp_alumno[1]:
        nota_final += 4
    elif resp_alumno[1] == "":
        nota_final += 0
    else:
        nota_final -= 1

    if resp_correctas[2] == resp_alumno[2]:
        nota_final += 4
    elif resp_alumno[2] == "":
        nota_final += 0
    else:
        nota_final -= 1

    if resp_correctas[3] == resp_alumno[3]:
        nota_final += 4
    elif resp_alumno[3] == "":
        nota_final += 0
    else:
        nota_final -= 1
    
    if nota_final < 0:
        nota_final = 0
    print(f'La nota final es {nota_final}')

calcular_nota(["a", "a", "b", "b"], ["a", "c", "b", "d"])
calcular_nota(["a", "a", "c", "b"], ["a", "a", "b", ""])
calcular_nota(["a", "a", "b", "c"], ["a", "a", "b", "c"])
calcular_nota(["b", "c", "b", "a"], ["", "a", "a", "c"])