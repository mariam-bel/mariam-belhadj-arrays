lista = []
max = float(input("Itroduce un número: "))
lista.append(max)
cont = 0
for i in range(9):
    num = float(input("Itroduce un número: "))
    lista.append(num)
for i in range(10):
    if lista[i]>max:
        cont = 1
        max = lista[i]
    elif lista[i]==max:
        cont +=1
print(f"{max} está repetido {cont} veces")