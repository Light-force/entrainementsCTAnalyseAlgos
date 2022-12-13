A = [0, 2, 4, 2, 2, 3, 1, 1, 5, 4, 1, 2, 3, 1, 2, 0]


def Algo():
    total = 0
    for i in range(1, len(A) - 2):
        maxGauche = 0
        maxDroite = 0
        for g in range(1, i):
            if A[g] > maxGauche:
                maxGauche = g
        for d in range(i + 1, len(A) - 2):
            if A[d] > maxDroite:
                maxDroite = d
        total += min(maxGauche, maxDroite) - A[i]
    return total


## NON FONCTIONNEL

print(Algo())
