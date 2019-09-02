# Afisarea cuvintelor ce apar de mai multe ori
# 21.08.2019
# Dragoi Octavian Marius

a = ("""nah maq vuh byk mys jep vuk meh zif nof buf bax gec zex nik nyq vuh lys jux gyk mys jex jyh bes biq veq gik lis myf vec zup gik bac jih nak vus zes baq bif vap guf jyh res gas nyh lic dof dyx rux gap roq les dix voh rus zax rus les gec gaq dyh gyq rot ves lus vis vec ret jof zyp gic bah rep mus zok nik dyf joc doh jyx rut giq nap juc leq vyk lis rys vek lak dax nuc bup jic nat lux zaq buq dac rik guh zif bif dyt baq nif rat jok mox nyq vic mif dec zep mut mux nuc lyk bok jeh nic nuk jax dep ves dyf zah muk jup dic bot juh lek myc nec mic dec neh guq doc lip jit box muk vyq lat mis rep noq dac zuk leh muq jep jos vex vak geh baq lah lak geq vuq rik nik diq max dyh vos jot nup jet zoq gek zos gyq jot zuc dox bup lek map boq meh rox dik joh les zuk vik ryt mip bat mif mot loq bys gyk lyt zit zix jeh zuq gas buk gut zis bys jyh bap buc gep jap zyq jux vot dih zyk nos mes jyf daf jic myq daf noq jex juf nak juf bop mot mos zih dap myf mip daf mic roh ryp mif zec gyp voq vih gis gec beh zuk duk vys veh lyh vic nux gek viq mit vuk bup vyx lus riq lap ziq rep lyk gax nyp nip gyh lih ros jix vaq zuf zop vak lix jyx nuf gif rut vef vys lah vyt noq bic muh zec gat zaf muk byc bet mak laf dac end""").split(" ")
b = []
for i in a:
    c = a.count(i)
    if c > 1:
        b.append(i)
b = set(b)
print(" ".join(sorted(b)))
