# Conversia unui numar in sistem binar
# 25.08.2019
# Dragoi Octavian Marius
a = "121165436 173 11701509 48875633 -86 -179583244 -1935522030 -12968521 1618 14 1087025912 -1412570 -764237 516 -9591 -6405 -63463 -9509130 62294 7 64933568 -194 10893 -1750 -484 126304269 -33 197685 102616 1185 -85969379 126171050 115445 -5910507 118 -7 106 873884 1115 -176 -14068 -114389747 -3833 -18894".split(" ")
a = list(map(int,a))
def binar(a):
    rez = []
    x = 0
    while x < 44:
        try:
            if a[x]< 0:
                b = bin(a[x]+(2**32)).replace("0b", "")
                d = b.count("1")
                rez.append(str(d))
                x= x+1
            else:
                b = "{:032b}".format(a[x])
                c = b.count("1")
                rez.append(str(c))
                x= x+1
        except IndexError:
            pass
    return rez
print(" ".join(binar(a)))
