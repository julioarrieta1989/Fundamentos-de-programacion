import funciones as f

tamaño = int(input("Ingrese tamaño del vector "))

vector = [0]*(tamaño+1)



f.llenarVector(vector,tamaño)

for i in range (1,tamaño+1):
   print(vector[i])


print(f"El tamaño del vector es {vector[0]}")
