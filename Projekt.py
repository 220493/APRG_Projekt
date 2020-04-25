"""volna_bunka = 0
blokovana_cesta = 1
i = hodnota v buňce testovacího bludiště"""

testovaci_bludiste = [[0,1,0,1,1], [0,0,0,0,0], [1,0,1,0,1], [0,0,1,0,0], [1,0,0,1,0]]
i = testovaci_bludiste[0] [0]
syr = testovaci_bludiste [-1] [-1]

ulozeni_reseni_1 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
j = ulozeni_reseni_1[0] [0]

"""soucast_cesty = 1
zbytek_bunek = 0
j = hodnota v buňce řešení"""

"""hledání cesty ven"""

"""x = souřadnice horizontálně"""
"""y = souřadnice vertikálně"""

x = 0
y = 0
"""myš x = 0, y = 0"""

def prvni_reseni(i,j,):
    while i == syr:
        pocetni_reseni_1 = 0
        pocetni_reseni_1 += sum(j)
        return pocetni_reseni_1
    else: kodove_reseni(i,j,x,y)

def kodove_reseni (i,j,x,y):
    while i == 0:
        j += 1
        x += 1
    else:
        x -= 1
        y -= 1
        if i == 0:
            j += 1
        else:
            y += 1
            x -= 1
            if i == 0:
                j += 1
            else:
                x += 1
                y += 1
                if i == 0:
                    j +=1
                else:
                    print("V bludišti neexistuje cesta k sýru.")












