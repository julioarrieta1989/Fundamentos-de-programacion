import random

def llenarVector(v,n):
    v[0]=n

    for i in range(1,n+1):
        v[i] = random.randint(1,20)
 



def imprimirVector(v):
    m=v[0]
    for i in range (1,m+1):
     print(v[i])

    print(f"El tamño del vector es {m}") 
 
  
def vectorVacio(v):
    if v[0]==0:
     return True

    return False 

 
 
   
def vectorLleno(v,n):
    if v[0]==n:
     return True

    return False 

 
def sumarVector(v):
    tamaño=v[0]
    total=0
    for i in range(1,tamaño+1):
        total=total+v[i]
    return total



def insertarDato(d,i,v,n):

    for j in range(v[0],i-1,-1): 
        v[j+1]=v[j]   
    v[i]=d
    v[0]=v[0]+1
