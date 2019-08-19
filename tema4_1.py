# Tema 4
# Dragoi Octavian Marius
# 13.08.2019

# 1
print ("\t\tLista de Cd-uri/Dvd-uri")
lista = []
dict_nou = {}
cheie = 0
titlu_nou = []
while (True):
    print("""            0 - Pentru afisare lista actuala
            1 - Pentru introducerea unui element nou
            2 - Pentru stergerea unui element existent
            3 - Pentru stergerea intregii liste
            4 - Cautare dupa titlu sau continut
            5 - Pentru iesire""")
    sir = input("\tAlgere o optiune\n")
    if sir.isdigit() and int(sir) < 6:
        if sir == "0":
            if (lista):
                print(dict_nou.keys(),"=>",dict_nou.values())
                print ("=>",lista)
            else:
                print("Lista si dictionarul sunt goale")
        elif sir == "1":
            val = input("Adauga valoarea dictionarului\n")
            dict_nou.__setitem__(cheie, val)
            cheie = cheie+1
            titlu = input("Adauga Titlu\n")
            if not titlu in titlu_nou:
                con = [input("Adauga continut\n")]
                con.insert(0,titlu)
                lista = lista + [con]
                titlu_nou.append(titlu)
            else:
                print("Nu poti adauga un titlu ce a fost deja adaugat")
        elif sir == "2":
            x = input("\tScrie numele elementului ce se va sterge\n")
            for x in lista:
                try:
                    lista.remove(x)
                except ValueError:
                    pass
                    print("Elementul",x,"a fost sters cu succes")
        elif sir == "3":
            dict_nou = {}
            lista = []
            print("\tLista si dictionarul au fost sterse")
        elif sir == "4":
            cauta = input("Scrie titlul sau continutul cautat\n")
            if any(cauta in x for x in lista):
                print("Elementul",cauta," a fost gasit in lista")
                print(lista)
            else:
                print("Elementul nu se afla in lista")
                print(lista)
        elif sir == "5":
            print("\t\tO zi buna!")
            break
        else:
            print("Nu ai introdus un caracter valabil")
