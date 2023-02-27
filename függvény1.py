def koszont( nev):
    print("Szia "+nev+"!")

koszont("Zoli")
koszont("Pista")

def dup(szam):
    szam = szam *2
    #print(szam)
    return szam

szam=12    
print(szam)
dup(szam)
print(szam)
print(dup(szam))

print(koszont("Pipacs"))
print(dup("alma"))

def paros(szam):
    if type(szam) == int:
        if szam % 2 == 0:
            return True
        else:
            return False

print(paros(13))
print(paros(12))
print(paros("aa"))
print(paros(12.45))

y=33
def localglobal(szam):
    x=szam  # local változó
    y=szam  # globális változó
x=12
localglobal(22)
print(x)
print(y)

def rekurziv(x):
    x+=1
    print(x)
    if x <= 10:
        rekurziv(x) 

rekurziv(1)

def fibbon(n1,n2,db):
    print(n1,n2)
    db+=1
    if db < 10:
        fibbon(n2,n1+n2,db )

fibbon(1,1,1)






