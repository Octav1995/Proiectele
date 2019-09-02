# Tema 5
# Dragoi Octavian Marius
# 26.08.2019

# 2
# Functii
tab = [["1","2","3"],["4","5","6"],["7","8","9"]]
numere = []
def intro():
    """ Afiseaza intro al jocului Tic-Tac-Toe."""
    return("""\t\tDoamnelor, domnisoarelor si domnilor,
va invit sa jucati Tic-Tac-Toe contra unui sistem automatizat care actioneaza
pe baza unui program de lucru stabilit sau mai pe intelesul tuturor, un robot.\n
\t\tJucatorul uman are dreptul de a incepe primul.""")

def rez():
    """Rezultatul jocului"""
    global numere
    if tab[1][1] == tab[0][0] == tab[2][2] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][1] == tab[0][0] == tab[2][2] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[1][1] == tab[0][2] == tab[2][0] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][1] == tab[0][2] == tab[2][0] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[1][1] == tab[0][1] == tab[2][1] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][1] == tab[0][1] == tab[2][1] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[1][0] == tab[0][0] == tab[2][0] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][0] == tab[0][0] == tab[2][0] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[1][2] == tab[0][2] == tab[2][2] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][2] == tab[0][2] == tab[2][2] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[2][0] == tab[2][2] == tab[2][1] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[2][0] == tab[2][2] == tab[2][1] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[0][0] == tab[0][2] == tab[0][1] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[0][0] == tab[0][2] == tab[0][1] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif tab[1][0] == tab[1][2] == tab[1][1] == "X":
        print("Jucatorul uman a invins! YAY!")
        exit()
    elif tab[1][0] == tab[1][2] == tab[1][1] == "O":
        print("Jucatorul robot a invins! Esti un umanoid nedemn de asa adeversar!")
        exit()
    elif len(numere) == 9:
        print("Meci egal!\nMult succes data viitoare!")
        exit()
    else:
        print("Lupta continua")
def body():
    """Jocul Tic-Tac-Toe - partea umana"""
    b = input("Pozitia elementelor pe tabla:\n1|2|3\n4|5|6\n7|8|9\nIntrodu un nr de la 1 la 9 pentru a adauaga un x:\n")
    if len(b) == 1 and b.isdigit() and b not in numere:
        numere.append(b)
        if b == "1":
            tab[0][0] = "X"
        elif b == "2":
            tab[0][1] = "X"
        elif b == "3":
            tab[0][2] = "X"
        elif b == "4":
            tab[1][0] = "X"
        elif b == "5":
            tab[1][1] = "X"
        elif b == "6":
            tab[1][2] = "X"
        elif b == "7":
            tab[2][0] = "X"
        elif b == "8":
            tab[2][1] = "X"
        elif b == "9":
            tab[2][2] = "X"
        for row in tab:
            print(row)
        return (rez())
    elif b in numere:
        print("Pozitia aleasa este deja ocupata")
        body()
    else:
        print("Nu ai introdus o cifra valabila")
        body()
def robo():
    """Jocul Tic-Tac-Toe - partea robot"""
    if tab[1][1] == "5":
        numere.append("5")
        tab[1][1] = "O"
    elif tab[0][0] =="1":
        numere.append("0")
        tab[0][0] = "O"
    elif tab[0][2] =="3":
        numere.append("3")
        tab[0][2] = "O"
    elif tab[2][0] =="7":
        numere.append("7")
        tab[2][0] = "O"
    elif tab[2][2] =="9":
        numere.append("9")
        tab[2][2] = "O"
    elif tab[0][1] =="2":
        numere.append("2")
        tab[0][1] = "O"
    elif tab[1][0] =="4":
        numere.append("4")
        tab[1][0] = "O"
    elif tab[1][2] =="6":
        numere.append("6")
        tab[1][2] = "O"
    elif tab[2][1] =="8":
        numere.append("8")
        tab[2][1] = "O"
    print("Alegerea robotului este:")
    for row in tab:
        print(row)
    return (rez())




# Afisare
print(intro())
while len(numere) < 9:
    print(body())
    print(robo())
