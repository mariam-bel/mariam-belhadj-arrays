import random as r
vector1 = []
vector2 = []
vector3 = []
for i in range(15):
    vector1.append(r.randint(0,100))
    vector2.append(r.randint(0,100))
    vector3.append(vector1[i]+vector2[i])
print(f"Vector1 = {vector1} \nVector2 = {vector2} \nVector3 = {vector3}")