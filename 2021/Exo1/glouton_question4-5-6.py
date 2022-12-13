A = [0, 2, 4, 2, 2, 3, 1, 1, 5, 4, 1, 2, 3, 1, 2, 0]


def algoMaxGauche():
    max = 0
    tableau = (len(A) - 2) * [0]
    for j in range(1, len(A) - 1):
        if A[j] > max:
            max = A[j]
            tableau[j - 1] = max
        else:
            tableau[j - 1] = tableau[j - 2]
    return tableau


def algoMaxDroite():
    max = 0
    tableau = (len(A) - 2) * [0]
    for j in range(len(A) - 2, 0, -1):
        if A[j] > max:
            max = A[j]
            tableau[j - 1] = max
        else:
            tableau[j - 1] = tableau[j]
    return tableau


def Algo():
    total = 0
    j = 0
    arrayMaxGauche = algoMaxGauche()
    arrayMaxDroite = algoMaxDroite()
    for i in range(1, len(A) - 2):
        temp = min(arrayMaxGauche[j], arrayMaxDroite[j]) - A[i]
        if temp > 0:
            total += temp
        j += 1
    return total


print(Algo())
