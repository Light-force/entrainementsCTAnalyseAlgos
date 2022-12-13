n = 9
T = [90, 150, 130, 50, 60, 140, 70, 80, 120]


def ButinMax(n, T):
    Opt = (n + 1) * [0]
    Maisons = (n + 1) * [True]
    Opt[1] = T[0]
    for i in range(2, n + 1):
        if Opt[i - 1] < (Opt[i - 2] + T[i - 1]):
            Opt[i] = Opt[i - 2] + T[i - 1]
        else:
            Opt[i] = Opt[i - 1]
            Maisons[i] = False
    return Opt[n], MaisonsCambriolees(Maisons)
def MaisonsCambriolees(Maisons):
    i = len(Maisons) - 1
    maisonsCambriolees = []
    while i > 0:
        if (Maisons[i]):
            maisonsCambriolees.append(i)
            i = i - 2
        else:
            i = i - 1
    maisonsCambriolees.sort()
    return maisonsCambriolees


print(ButinMax(n, T))
