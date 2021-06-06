import random

def llenarVector(v,n):
    v[0]=n

    for i in range(1,n+1):
        v[i] = random.randint(1,99)
 



def imprimirVector(v):
    m=v[0]
    for i in range (1,m+1):
     print(v[i])

    print(f"El tamño del vector es {m}") 
 
  


 

 