# Mesaj codificat
# 27.08.2019
# Dragoi Octavian Marius

mesaj = ("""PK QO EJ KHZAJ OPKNEAO WJZ OK UKQ PKK XNQPQO PDA OAYNAP KB DAWPDAN WHA.
PDWP WHH IAJ WNA YNAWPAZ AMQWH IAP W SKIWJ WP PDA SAHH.
YWHHAZ EP PDA NEOEJC OQJ.
W ZWU WP PDA NWYAO EJ WJYEAJP LANOEW PDANA SWO W GEJC.
PDA ZAWZ XQNU PDAEN KSJ ZAWZ.""").casefold()
mesaj = mesaj.split("\n")
f = []
r =[]
for p in mesaj:
    h =list(map(ord,p))
    f.append(h)
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result
for i in flatten(f):
    if i == 46 or i ==32:
        pass
        r.append(i)
    elif i+4>122:
        i = i-22
        r.append(i)
    else:
        i = i+4
        r.append(i)
print("".join(list(map(chr,r))).upper())
