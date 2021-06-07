class vector:

 def __init__(self, n):
   self.n=n
   self.V=[0]*(n+1)

 def Tamaño(self):
     
    return self.n


v=vector(2) 
for i in range(1,4+1):
  numero = int(input("Ingrese un numero "))
  v.V[i]=numero

  print(v.V[i])

print(v.Tamaño() ) 