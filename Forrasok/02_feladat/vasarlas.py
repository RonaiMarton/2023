"""Írjon programot vasarlas.py néven, ami billentyűzetről bekéri egy termék árát forintban, az euro árfolyamát és egy euro összeget, 
majd kiírja a minta szerint, hogy a beírt euroért meg tudjuk-e vásárolni a terméket. 
Minta:
Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 50
A terméket meg tudod vásárolni!

Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 5.15
Nincs elég euród a termék megvásárlására!
"""

termek_ar = int(input("Adja meg a termék árát forintban \n"))
euro_arfolyam = float(input("Kérem adja meg az euró árfolyamát \n"))
vasarlo_euroja = float(input("Adja meg, hogy mennyi erurója van \n"))

termek_ara_euroban = termek_ar / euro_arfolyam

if termek_ara_euroban< vasarlo_euroja:
    print("Elegendő eurója van")
else:
    print("Nincs elegendő eurója")