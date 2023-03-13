import random
szavak=["alma","pipacs","szilva","kalap","kapa"]

szo = szavak[random.randrange(5)]
print(szo)
tovabb=True
db=0
while tovabb:
    kar=input("Kérek egy betűt: ")
    if kar=="":
        tovabb=False
    else:
        if szo.find(kar)>=0:
            print(kar)
            db+=1
            if db == len(szo):
                tovabb=False
                print("Összes betűt ismered")
