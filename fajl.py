f = open("1.csv")

print(type(f))

print(f.read()) #a fájl összes elemét kiírja
f.seek(0) # sor elejére megy
print(f.read())

f.seek(2)
print(f.read())

f.seek(0) 
print(f.readline()) #a sorokat írja ki
print(f.readline())
print(f.readline())
print(f.readline())
print("----------------")


f.seek(0)

for sor in f: #kiírja a sorokat
    print(sor)
print("----------------")


f.seek(0)
for sor in f:
    print(sor.replace('\n','')) #kiírja a sorokat sortörés nélkül

print("----------------")

f.seek(0)
teszt=f.read() #stringben írja ki a sorokat
print(type(teszt))
print(teszt)

print("----------------")

f.seek(0)
teszt=f.readlines() #listában írja ki a sorokat (egy sorban)
print(type(teszt))
print(teszt)

print("----------------")

adatsorok = []
f.seek(0)
for sor in f:
    adatsorok.append(sor.replace('\n','')) # listában írja ki a sorokat (\n) nélkül

print("----------------")

print(adatsorok)

adatsorok = []
f.seek(0)
for sor in f:
    adatsorok.append(sor.replace('\n','').split(',')) #listában listát csinál

print("----------------")

print(adatsorok)

print(adatsorok[0]) # a megadott sor írja ki
print(adatsorok[0][0]) # a megadott sorban az első elemet írja ki 

print("----------------")

for sor in adatsorok: # kiírja az elemeket a listában egyesével
    for elem in sor:
        print(elem,end=" ")







f.close()

