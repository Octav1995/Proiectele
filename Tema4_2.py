# Tema 4
# Dragoi Octavian Marius
# 12.08.2019

# 2
fisier = open("Text_clasa.ini", "w")
text = ["Nume Prenume Student\n","Ini, text sau txt\n","Citire\n"]
fisier.writelines(text)
fisier.close()

fisier = open("Text_clasa.ini", "r")
lista = list(fisier)
print(lista)
fisier.close()

fisier = open("Text_clasa.ini", "a")
text_2 = ("<<EU SUNT 4>>\n")
fisier.write(text_2)
fisier.close()

fisier = open("Text_clasa.ini", "r")
citire = fisier.read()
print(citire)
fisier.close()
