'''szam=int(input("Kérek egy természetes számot: "))
# print(szam % 2)
if szam % 2 == 0:
    print("A "+str(szam)+" páros")
    print("A ",szam,"páros")
else:
    print("A "+str(szam)+" páratlan")


szam=int(input("Kérek egy természetes számot: "))
if szam % 2 == 0:
    print("A ",szam," páros")
elif szam % 3 == 0:
    print("A",szam,"hárommal osztható")

if szam % 2 == 0 and szam % 3 == 0:
    print("A ",szam,"osztható 6-al")    


if -1 :
    print(1)

print( 13 % 2 == 0)
print( True == 1)
print( False == 0)'''


import random

random_szam = random.randint(1,100)
print(random_szam)      

