tovabb=True

l=[]
def minimum(lista):
    #return min(lista)
    m=lista[0]
    for s in lista:
        if s<m:
            m=s
    return  m

while(tovabb):
    szam=int(input("Kérek egy pozitív számot: "))
    if szam < 0 :
        tovabb=False
    else:
        l.append(szam)

print(minimum(l))
