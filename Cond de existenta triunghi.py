# Conditia de existenta a unui triunghi
# 26.08.2019
# Dragoi Octavian Marius
a = ("""102 296 173
1178 915 1734
253 554 425
930 2100 1014
342 460 226
184 204 111
997 993 799
2677 1106 956
414 231 161
243 290 715
818 991 807
1118 490 504
478 270 210
273 558 254
697 1514 588
1707 701 862
594 353 505
634 1088 341
928 1838 772
272 390 627
775 2335 1108
276 331 694
851 963 1362
917 1486 751
2743 802 1563
2709 1379 848
274 545 1316""").split("\n")
b =[]
r = []
a = [i.split(" ") for i in a]
for i in a:
    c = list(map(int,i))
    b.append(c)
print(b)
for x in b:
    if sum(x)-max(x)>max(x) or sum(x)-max(x)==max(x) :
        r.append("1")
    else:
        r.append("0")
print(" ".join(r))
