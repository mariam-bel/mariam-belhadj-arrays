nalumnos = int(input("Introduce el número de alumnos: "))
estaturas = []
aux = 0
cont1=0
cont2=0
for i in range(nalumnos):
    estaturas.append(int(input("Introduce la estatura de cada alumno en centímetros: ")))
    aux += estaturas[i]
for i in range(nalumnos):
    if estaturas[i]>=aux/nalumnos:
        cont1 += 1
    else:
        cont2 += 1
print(f"{estaturas}\nHay {cont1} alumnos que superan o miden igual a la media y {cont2} que son más bajos.")