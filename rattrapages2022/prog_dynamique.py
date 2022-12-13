n = 9
T = [90, 150, 130, 50, 60, 140, 70, 80, 120]


def ButinMax(n, T):
    Opt = (n + 1) * [0]
    Opt[1] = T[0]
    for i in range(2, n + 1):
        Opt[i] = max(Opt[i - 1], Opt[i - 2] + T[i - 1])
    return Opt[n]


print(ButinMax(n, T))
