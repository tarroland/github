# függvényekről
def teszt(nev):
    print("Szia "+nev+"!")

teszt("Pisti")
teszt("Zoli")
teszt("Karcsi")
teszt("Ági")
# print(nev)
def negyzet(x):
    n=x*x
#    print(n)
    return n

negyzet(3)
print(negyzet(3))

harom=negyzet(3)
negy=negyzet(4)
ot=negyzet(5)
print((harom+negy)/ot)

for i in range(1,101):
    x=negyzet(i)
    print(i,x)
print(x)    



def kiIr(lista):
    for x in lista:
        print(x,end=",")
    print()

print("---------------")
l = list()
l = [1,12,2,3]
print(l[3])
print("---------------")

def kiIr2(lista):
    for i in range(len( lista)):
        print(lista[i])



en_listam=(1,2,3,4,2,3)
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
kiIr2(en_listam)

en_listam=[1,2,3,4,2,3]
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
kiIr2(en_listam)

en_listam={1,2,3,4,2,1}
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
#kiIr2(en_listam)


def add(a,b):
    return a+b

def add(a,b,c):
    return a+b+c

def add(a,b,c,d):
    return a+b+c+d


#print(add(1,2))
#print(add(1,2,3))
print(add(1,2,3,4))
#print(add(1,2,3,4,5))


def add2(*szam):
    osszeg=0
    for x in szam:
        osszeg+=x
    #print(type(szam))
    return osszeg

print(add2(1))
print(add2(1,2))
print(add2(1,2,3,4,5))

#print(add2("a","b"))


