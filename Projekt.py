"""Bludiště
myš je v bludišti x = 0, y = 0
hodnoty jednotlivých polí:
0 - prázdná buňka
1 - zeď nebo ohraničení bludiště
2 - navštívená buňka
3 - koncová buňka"""

bludiste = [[0,1,0,1,1],
            [0,0,0,0,0],
            [1,0,1,0,1],
            [0,0,1,0,0],
            [1,0,0,1,3]]
x = 0
y = 0

cesta_bludistem = []

def reseni():
    while bludiste [x] [y] == 3:
        seznam_vysledku = []
        ciselna_hodnota = 0
        ciselna_hodnota += sum(int(True))
        seznam_vysledku.append(ciselna_hodnota,"""+ další řešení...díky procházení cesty v jiném pořadí""")
        if ciselna_hodnota == min(seznam_vysledku):
            if bludiste [x] [y] == True:
                cesta_bludistem [x] [y] = 1
            else:
                cesta_bludistem [x] [y] = 0
        else:
            print("Z bludiště nevede cesta ven.")
    else: cesta(x, y)

def cesta(x, y):
    if bludiste [x] [y] == 1:
        return False
    elif bludiste [x] [y] == 3:
        return True
    elif bludiste [x] [y] == 2:
        return False
    else:
        bludiste [x] [y] = 2
        if (((x < len(bludiste)-1 and cesta(x + 1, y))
            or (y > 0 and cesta(x, y - 1))
            or (x > 0 and cesta(x - 1, y))
            or (y < len(bludiste)-1 and (x, y + 1)))):
            return True
        else:
            return False










