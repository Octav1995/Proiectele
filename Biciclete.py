# Cursa de biciclete
# 28.08.2019
# Dragoi Octavian Marius

a ="""224 18 11
27 21 25
51 10 18
65 23 11
24 26 11
15 13 26
54 29 13
20 14 10
14 11 20
332 15 17
26 25 14
53 15 28
13 29 26
29 21 17
37 20 26
183 27 26
30 16 14
75 21 29
136 12 17
55 14 15""".splitlines()
f = [i.split(" ")for i in a]
b = []
p = []
for i in f:
    fb = list(map(int,i))
    b.append(fb)
def bic(k):
    x =k[0]/(k[1]+k[2])
    return x*k[1]
for i in b:
    r =(bic(i))
    p.append(r)
p = list(map(str,p))
print(" ".join(p))
