szoveg=input("Kérek egy szöveget: ")
eDb=0
for c in szoveg:
    if c=='e':
        eDb+=1;
print(eDb," darab 'e' betű volt")

db=0
for c in szoveg:
    if c=='a':
        print("a .",db)
    if c=='e':
        print("e .",db)
    if c=='i':
        print("i" ,db)
    if c=='o':
        print("o ", db)
    if c=='u':
        print("u",db)
    db+=1