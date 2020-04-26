"""x = souřadnice horizontálně"""
"""y = souřadnice vertikálně"""

x = 0
y = 0
"""myš x = 0, y = 0"""

"""volna_bunka = 0
blokovana_cesta = 1
i = hodnota v buňce testovacího bludiště"""

testovaci_bludiste = [[0,1,0,1,1], [0,0,0,0,0], [1,0,1,0,1], [0,0,1,0,0], [1,0,0,1,0]]
i = testovaci_bludiste[x] [y]
testovaci_bludiste [-1] [-1] = 1000000
syr = testovaci_bludiste [-1] [-1]

"""syr = testovaci_bludiste [-1] [-1]"""

ulozeni_reseni_1 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
j = ulozeni_reseni_1[x] [y]

"""soucast_cesty = 1
zbytek_bunek = 0
j = hodnota v buňce řešení"""

"""hledání cesty ven"""

def prvni_reseni(i,j):
    while i == syr:
        pocetni_reseni_1 = 0
        pocetni_reseni_1 += sum(range(j))
        return pocetni_reseni_1
    else: kodove_reseni(i,j,x,y,z,c)

z = 1
c = z + 1
def kodove_reseni (i, j, x, y, z, c):
    while i == 0:
        j += 1
        x += 1
        if i != 0:
            x -= 1
            y -= 1
            if i == 0:
                return
            else:
                 y += 1
                 x -= 1
                 if i == 0:
                     return
                 else:
                     x += 1
                     y += 1
                     if i == 0:
                         return
    else:
        y -= 1
        if c != len(testovaci_bludiste [0]):
            x += c
            if i == 0:
                return
            else:
                x -= c
                y -= c
                if i == 0:
                    return
                else:
                    y += c
                    x -= c
                    if i == 0:
                        return
                    else:
                        x += c
                        y += c
                        if i == 0:
                            return
                        else:
                            z += 1
        else:
            print("Bludiště nemá východ")

print(prvni_reseni(i,j))
"""def ostatni_reseni():
    dalsi_reseni = -1
    return dalsi_reseni

def vysledne_reseni (pocetni_reseni_1, dalsi_reseni):
    prvni_reseni(i,j)
    ostatni_reseni()
    hodnoty_reseni = []
    hodnoty_reseni.append(int(pocetni_reseni_1))
    hodnoty_reseni.append(int(dalsi_reseni))
    hodnoty_reseni.sort()
    return hodnoty_reseni"""

"""print("Nejkratší cesta bludištěm:")"""










