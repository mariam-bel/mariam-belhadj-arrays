import random as r
lista = []
for i in range(10):
    lista.append(r.randint(0,100))
print(lista)
for i in range(len(lista)):
    if(lista[i]%2==0):
        print(f"{lista[i]} es par y está en la posición {i}")