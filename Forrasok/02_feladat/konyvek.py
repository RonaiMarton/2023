"""
•	A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például:3. feladat:)! 
•	Az egyes feladatokban a kiírásokat a minta szerint készítse el!
•	Az ékezetmentes kiírások is elfogadottak.
•	Az azonosítókat kis betűkkel is kezdheti.
•	A program megírásakor az állományban lévő adatok helyes szerkezetét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.
•	Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemeneti adatok mellett is helyes eredményt adjon!
1.	Készítsen programot a következő feladatok megoldására, melynek kódját nagykonyv.py néven mentse el. Olvassa be az UTF-8 kódolású konyvek.txt állományban lévő adatokat és tárolja el egy saját osztály (konyv) típusú listában! Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza! Az élő íróknak nincs megadva halálozási év. Az adatok tárolásakor ezeknél az íróknál a 2005-ös évet tárolja el halálozási évként!
2.	Hány könyv adatai szerepelnek az állományban?
3.	Írja ki a legjobb helyezést elért magyar könyv adatait a minta szerint!
4.	Bekerült-e a listába német nemzetiségű író könyve?
5.	Listázza ki az 90 évesnél idősebb írókat. A kortárs íróknál (akiknél nem szerepel halálozási év) a 2005-ös évet használja az életkor számításához! Ügyeljen arra, hogy a kiírásnál minden író csak egyszer szerepeljen! Az írók nevének sorrendje tetszőleges lehet.

"""
konyvek = []
# with open(r'Forrasok\02_feladat\konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
with open(r'Forrasok\02_feladat\konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
        next(forrasfajl)
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            #nev;szulEv;halEv;nemzetiseg;cim;helyezes
            nev = adatok[0]
            szulEv = int(adatok[1])
            halEv = int(adatok[2])   if adatok[2] != ""  else 2005
            nemzetieseg = adatok[3]
            cim = adatok[4]
            helyezes = adatok[5]
            konyv = {'nev' : nev, 'szulEv' : szulEv, 'halEv' : halEv, 'nemzetiseg' : nemzetieseg, 'cim' : cim, 'helyezes' : helyezes}
            konyvek.append(konyv)

#print(f'{konyvek=}')

#3.2
print(f"3.2 feladat. Az állományban {len(konyvek)} db könyv adatai szerepelnek")

#3.3
magyar_konyvek = []
for konyv in konyvek:
      if konyv['nemzetiseg'] == "magyar":
            magyar_konyvek.append(konyv)
# print(f"{len(magyar_konyvek)}")

legjobb_konyv = magyar_konyvek[0]
for konyv in magyar_konyvek:
      if konyv['helyezes'] < legjobb_konyv['helyezes']:
            legjobb_konyv = konyv
print(f"{legjobb_konyv['nev']} : {legjobb_konyv['cim']} a legjobb magyar könyv")

#3.4
for konyv in konyvek:
    if konyv['nemzetiseg'] == "német":
        van_nemet = "Van német író a listában"
        break
    else:
        van_nemet = "Nincs német író a listában"
print(van_nemet)

#3.5
idosebb_mint_kilencven = set()
for konyv in konyvek:

    eletkor = konyv['halEv'] - konyv['szulEv']
    if eletkor >= 91:
        idosebb_mint_kilencven.add(konyv['nev'])
# print(idosebb_mint_kilencven)
print(f"Ezek az emberek idősebbek, mint 90:")
for iro in idosebb_mint_kilencven:
    print("\t" + iro)
