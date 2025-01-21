import random as r
vector = []
for i in range(10):
    vector.append(r.randint(0,100))
print(vector)
pos = int(input("Introduce una posición: "))
vector.pop(pos-1)
print(vector)