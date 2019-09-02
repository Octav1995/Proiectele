# Calculul unor progresii aritmetice
# 22.08.2019
# Dragoi Octavian Marius

a = ("""2 16 20
9 19 49
21 20 69
7 15 35
8 11 86
15 11 67
28 19 32
11 8 61
18 2 10
2 5 33""").replace("\n"," ")
a = a.split()
a = list(map(int,a))
c = 2
nr = 0
d = 1
e = 0
set =set()
res =[]
for i in a:
    try:
        while nr < a[c]:
            su = a[e]+(nr*a[d])
            set.add(su)
            nr = nr+1
    except IndexError:
        pass
    else:
        res.append(sum(set))
        c += 3
        e += 3
        d += 3
        nr = 0
        set = {0}
        continue
res = list(map(str,res))
print(" ".join(res))
