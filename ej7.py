import random as r
vector = []
for i in range(10):
    vector.append(r.randint(0,100))
print(vector)
num = int(input("Introduce un número: "))
pos = int(input("Introduce una posición: "))
vector[pos-1]=num
print(vector)