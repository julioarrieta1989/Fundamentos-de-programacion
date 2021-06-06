import ramdom

def llenarVector(v,n):
    v[0]=n

    for i in range(1,n+1):
        v[i] = random.randint(1,99)
