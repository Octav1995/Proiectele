
# Dragoi Octavian Marius
# 25.07.2019

# 1
print("\t\tProgram ce verifica tipul textului introdus")
sir = input("Introduceti sirul de caractere\n")
if sir.isdigit():
    print("Sirul de caractere este format din numere",sir.center(80))
elif sir.isalpha():
    print("Sirul de caractere este format din litere",sir.swapcase())
else:
    print("Sirul de caractere este format din diverse elemente", "#!".join(sir))


# 2
print("Calculator pentru formula {6*[2+(a-1)%b]*2**a}\n")
a = (input("Introduceti o valoare pentru a\n"))
b = (input("Introduceti o valoare pentru b\n"))
if a.isalpha() and b.isalpha() or a.isspace() and b.isspace():
    print("Caracterele introduse nu sunt cifre")
elif float(a) == 0 or float(b) == 0:
    print("Nu se poate atribui valoare 0 lui a sau b")
elif float(a) and float(b):
    a = float(a)
    b = float(b)
    ab = (6*(2+(a-1)%b)*2**a)
    print("Rezultatul calculat este", ab)


# 3
print("\t\tAfla daca un numar este par sau impar")
nr = input("Introduceti un numar\n")
if nr.isdigit():
    nr = int(nr)
    if nr % 2 == 0:
        print("Numarul ales este par")
    else:
        print("Numarul ales este impar")
else:
    print("Caracterele introduse nu sunt numere intregi pozitive")


# 4
print("\t\tSir de caractere")
caract = input("Introduceti un sir de caractere\n")
if "este" in caract and caract.endswith(("!","?",".",",")):
    print("Cuvantul este s-a gasit si sirul se termina cu . , ! sau ?")
elif "este" in caract:
        print("Cuvantul este se gaseste in sir")
else:
    print("Sirul nu contine cuvantul este")


# 5
print("\t\tAfla care sunt anii bisecti")
an = input("Introduceti un an\n")
if an.isdigit():
    an = int(an)
    if an % 4 == 0:
        print("Anul introdus este an bisect")
    else:
        print("Anul introdus nu este an bisect ")
else:
    print("Caracterele introduse nu sunt numere pozitive")


 # 6
numar =input("Introduceti un numar\n")
if numar.isalnum() and numar.isalpha() or numar.isspace():
     print("Caracterele introduse nu sunt cifre")
elif float(numar) == 0:
     print("Numarul este 0")
elif float(numar) < 0:
     print("Numarul este negativ, valoarea absoluta fiind", abs(float(numar)))
elif 0 < float(numar) < 10:
      print("Numar intre 0 si 10")
elif float(numar) > 10:
      print("Numar mai mare ca 10")


# 7
print("\t\tMeniu""""\n1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Stegere lista de cumparaturi
5 - Cautare in lista de cumparaturi""")
meniu = input("Apasa tastele 1 - 5 pentru a alege optiunea dorita\n")
if meniu.isdigit() and int(meniu) == 1:
    print ("Aceasta este lista dumneavoastra de cumparaturi")
elif meniu.isdigit() and int(meniu) == 2:
    print ("Adaugati elementul dorit")
elif meniu.isdigit() and int(meniu) == 3:
    print("Stergeti elemenul dorit")
elif meniu.isdigit() and int(meniu) == 4:
    print("Stergeti lista de cumparaturi")
elif meniu.isdigit() and int(meniu) == 5:
    print("Adaugare element")
else:
    print("Alegerea nu exista. Reincercati.")
