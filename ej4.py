lista = []
par = 0
impar = 0
for i in range(10):
    lista.append(int(input()))
for i in range(len(lista)):
    if(i%2==0):
        par += lista[i]
    else:
        impar += lista[i]
print(f"La media en las posiciones pares es: {par/5}")
print(f"La suma en las posiciones impares es: {impar/5}")