notas = []
suma = 0
aprobados=0
suspensos=0
supera=0
for i in range(40):
    notas.append(int(input(f"Introduce la nota del alumno {i}: ")))
    suma += notas[i]
for i in range(40):
    if notas[i]>=5:
        aprobados+=1
        if notas[i]>suma/40:
            supera += 1
    else:
        suspensos+=1
print(f"{aprobados} alumnos han aprobado, {suspensos} han suspendido y {supera} superan la nota media de la clase, que es {suma/40}.")