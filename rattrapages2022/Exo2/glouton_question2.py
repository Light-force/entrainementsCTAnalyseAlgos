L = [[10, 300], [2, 40], [8, 200], [5, 150], [1, 40], [7, 140]]


def algoMaxGauche():
    max = 0
    tableau = len(L) * [[0, 0]]
    for i in range(0, len(L)):
        if (L[i][0] * L[i][1]) > max:
            max = L[i][0] * L[i][1]
            tableau[i] = [L[i][0], L[i][1]]
        else:
            tableau[i] = [tableau[i - 1][0], tableau[i - 1][1]]
    return tableau


def algoMaxDroite():
    max = 0
    tableau = len(L) * [[0, 0]]
    for i in range(len(L) - 1, -1, -1):
        if (L[i][0] * L[i][1]) > max:
            max = L[i][0] * L[i][1]
            tableau[i] = [L[i][0], L[i][1]]
        else:
            tableau[i] = [tableau[i + 1][0], tableau[i + 1][1]]
    return tableau


def algoMaxSalaire(T):
    total = len(L) * [0]
    arrayMaxGauche = algoMaxGauche()
    arrayMaxDroite = algoMaxDroite()
    for i in range(0, len(L)):
        temp = T - min(arrayMaxGauche[i][0], arrayMaxDroite[i][0])
        if temp >= 0:
            T -= min(arrayMaxGauche[i][0], arrayMaxDroite[i][0])
            total[i] = min(arrayMaxGauche[i][0], arrayMaxDroite[i][0])
    return total


print(algoMaxSalaire(20))
