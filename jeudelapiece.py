moy = 0

for i in range(10):
    n = 1000000
    gain = 0

    for i in range(n):
        jeu = pieceEquilibre()
        if jeu == 1:
            gain += pieceJeuA()
        else:
            if gain % 3 == 0:
                gain += pieceJeuB1()
            else:
                gain += pieceJeuB2()
    moy += gain
    
print("le gain net est de :", moy /10, "€")
