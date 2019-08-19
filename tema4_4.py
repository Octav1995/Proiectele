# Tema 4
# Dragoi Octavian Marius
# 13.08.2019

# 4
file = open("Tema3.txt","r+")
cit = file.read()
cuvant = input("Cuvantul cautat este:\n")
if cuvant in cit:
    try:
        count = cit.count(cuvant)
        print("Cuvantul a fost gasit de",count,"ori")
    except Exception:
        print("Nu am gasit cuvantul in text")
file.close()
