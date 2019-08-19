# Tema 4
# Dragoi Octavian Marius
# 12.08.2019

# 6
lista = []
while (True):
    a = input("Introdu un nr. intreg sau q pentru iesire:\n").lower()
    if a.isdigit():
        lista.append(int(a))
        minim = min(lista)
        maxim = max(lista)
        print("Nr. minim este",minim,"Nr. maxim este",maxim)
    elif a == "q":
        break
    else:
        print ("Nu ai introdus un caracter valid")
