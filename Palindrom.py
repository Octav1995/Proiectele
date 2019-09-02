# Verificare cuvinte palindrom
# 24.08.2019
# Dragoi Octavian Marius

a= ("""Lkqc-Uwwlzr-Vtwg-wtv-Rzl, wwu-c-Qk-l
Usbsyqdvnbevnsow, Bdebye Yy, s Yye yb, edbwosnvebnv, Dqysbsu
Ksm aeku hnaz, oo, Zanhuk eamsk
A-B, uodu-d Xu mae, ej, e Eayuxd-Ud-Ouba
I, T, Oxa Eyook Rdb, zbdr-Ko, Oyeax-oti
A Opdalr, Kjcai-Pdyly, dpiacjk R, laduoa
Bk, H Yi o yoiyhk, b
Irzfvsre-Avurvvruvaersvfz-ri
R-Iyaa, Pzdjs-W, Psruiliurapwsj-dzpaayir
Uy goxhy-Cyhxo, Gu
Hqrrotautla-Iezouok-Aowwoako-Uozeialt, UatorrkQh
Ijbfoil-cyuojuuuj-Ouycliofbji
Mt ex,aup, gduo qou dgpux-e-tm
Fgfjdhoqdngfrzgn dqoh, D Jf-gf
Yqaiyoohuceywsbsjauljuyyujbuajsbswyecuhooyi-Aqy
Ib-gseilkvngnoaaong, Nvk-Li, Esg Bi""").casefold()
a=a.replace(",","")
a=a.replace(" ","")
a=a.replace("!","")
a=a.replace(" ","")
a=a.replace("-","")
a=a.split("\n")
lista =[]
for i in a:
    if i[0::] == i[::-1]:
        b='Y'
        lista.append(b)
    else:
        c='N'
        lista.append(c)
print(" ".join(lista))
