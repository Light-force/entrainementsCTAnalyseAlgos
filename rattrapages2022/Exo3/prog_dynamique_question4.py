n = 9
T = [90, 150, 130, 50, 60, 140, 70, 80, 120]


def ButinMax(n, T):
    Opt = (n + 1) * [0]
    for i in range(0, n + 1):
        if i <= 2:
            Opt[i] = T[i - 1]
        else:
            Opt[i] = max(Opt[i - 1], Opt[i - 2] + T[i - 1])
    return Opt[n]


print(ButinMax(n, T))
