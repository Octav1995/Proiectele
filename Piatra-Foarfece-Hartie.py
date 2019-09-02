# Afiseaza invingatorul unei serii de Rock-Paper-Scissors
# 27.08.2019
# Dragoi Octavian Marius

import collections
import statistics
from collections import Counter
a = ("""PP PR SR RR SR SP PR SP
RR PS RS SR PP SS RR RP SP PS SP SS RR PP RS RR SP
SP SR RP RS SR
PR PS RR PS SS RR RR RP
SS PS RR SR SR RP
RS PP SP PR RP SR SR PS
PS PR PS PP RR PR SS RS RS PP PP SS PR
PP SR RP PR RR PP RS RP PS PR RR SS SR SS PS
RP PR PR SS RS PS RR SP SS RR RP SS RR PS SP
SS SR PS SP RS SS RR SS RP SR
RR PP RR RS PP SP RS RR SP RS
SS SP PS RP SS PS PR RP RS RS SS RP
RP PP PR PR SS SP RR PR SP PS PS RR RS
SS PS SR PP PP SS PP PR SS PS SS RP RR PP PP PP RS PR RS PP PR PR
RR PS PP PP SR PR SR PR PR RP PP PP SR RS SR
SR RP PS RS PP PP RP RP
RS PS RR RS RR SS PP PP PR RP PS SS PP RR SP SR PP SP PR
PP SP SP RR RP RP RR PR SS RS
SS SR RP SP SS RR SS SR RR PP PS PP RS PR RR SS SS RS PS
RS PR SP RR PR
SP PP RP RP SR SS RP PP PS
SS PP RR SR PP PS PR RR PS RR SP SP SR
PS SS PS RR RP
PS PS SS SR
PS RP SS RR SP RP RR RS RP SR RR SS SP PS""").split("\n")
a = [i.split(" ")for i in a]
b =[]
def win(l=[]):
    h=[]
    for i in l:
        if i=="PP" or i=="RR" or i=="SS":
            pass
        elif i=="SP" or i=="PR" or i=="RS":
            h.append("1")
        elif i=="PS" or i=="RP" or i=="SR":
            h.append("2")
    w = collections.Counter(h)
    most_common = Counter(h).most_common(1)[0][0]
    return(str(most_common))
for q in a:
    b.append(win(q))
print(" ".join(b[0:25]))
