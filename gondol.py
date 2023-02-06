import random
# random.seed(0)

# kor = input("Add meg az életkorod: ")
kor = 50
if kor > 10:
    kor=kor-10

gondolt = random.randint(1,100+kor*10)
print(gondolt)
 
# tipp = int(input("Kérem a tipped"))
'''
ismetles = True
while (ismetles):
    tipp = input("Kérem a tipped: ")
    tipp = int(tipp)

    if tipp < gondolt:
        print("Kicsi")
    if gondolt < tipp:
        print("Nagy")
    if gondolt == tipp:
        print("Talált")
        ismetles = False
'''

db=0
tipp = 0
while (tipp != gondolt):
    tipp = int(input("Kérem a tipped: 1 és "+str(100+kor*10)+" között"))
    # db +=1
    db = db + 1
    if tipp < gondolt:
        print("Kicsi")
    else:
        if gondolt < tipp:
            print("Nagy")
print(db,"Lépésben talált")


