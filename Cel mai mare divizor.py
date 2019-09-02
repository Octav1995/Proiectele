# Cel mai mare si cel mai mic divizor comun
# 25.08.2019
# Dragoi Octavian Marius

import math
a =("""2700 2610
720 300
42 29
3000 4500
5376 4452
562 9021
8 250
1308 180
1394 2584
86 8608
58 126
1548 1314
598 918
975 1248
3589 1739
2418 806
190 375""").splitlines()
a = [i.split(" ")for i in a]
b = []
c = []
for y in a:
    a = list(map(int,y))
    b.append(a)
for i in b:
    v =math.gcd(i[0],i[1])
    j =i[0]*i[1]/v
    k ="("+str(v)+" "+str(int(j))+")"
    c.append(k)
c = list(map(str,c))
print(" ".join(c))
