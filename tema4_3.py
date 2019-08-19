# Tema 4
# Dragoi Octavian Marius
# 13.08.2019

# 3
file = open("Tema3.txt","a")
while (True):
    text = input("Introdu text in fisierul Tema3 si apasa q pentru iesire\n")
    if "info" in text.lower():
        file.write("\n")
        file.write("\n")
        file.write(text)
        print("info este in paragraf")
    elif text == "q":
        break
        print("La revedere")
    else:
        file.write(text)
        print("info nu este in paragraf")
file.close()
