import random
szamok=[]
for i in range(5):
    szamok.append(random.randrange(1,7))
szam=int(input("Kérek egy számot: "))
van=False
for i in range(5):
    if szamok[i] == szam:
        van=True
    
if van:
    print("A listában van")    
print(van,szamok)
