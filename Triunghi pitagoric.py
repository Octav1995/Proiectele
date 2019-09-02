# Verificare daca un triunghi este pitagoric/obtuz,ascutit
# 23.08.2019
# Dragoi Octavian Marius

input = ("""792, 1485, 1767,132, 99, 165,704, 1320, 1496,632, 1185, 1461,168, 576, 607,175 ,600, 625,816, 340, 950,425, 1020, 1174,396, 297, 428,140, 480, 487,1248, 364, 1333,564, 235, 599,560 ,1050, 1190,504, 945, 1071,180, 96, 191,92 ,69, 137,330 ,792, 858,20 ,15, 28,388, 291, 485,768, 1440, 1679,432, 810, 918,469, 1608, 1626,497 ,1704, 1785,528, 220, 547""").split(",")
a = 0
b = 1
c = 2
for i in input:
    try:
        ipotenuza = int(input[c])
        c1 = int(input[a])
        c2 = int(input[b])
        ip = ipotenuza*ipotenuza
        cc1 = c1*c1
        cc2 = c2*c2
        if ip == cc1+cc2:
            print(" P ")
        elif ip < cc1+cc2:
            print(" A ")
        elif ip > cc1+cc2:
            print(" O ")
        a += 3
        b += 3
        c += 3
    except IndexError:
        pass
