T = [90, 150, 130, 50, 60, 140, 70, 80, 120]


def butinMax(T):
    maison = []
    Sol = []
    for i in range(len(T)):
        Sol.append(0)
    for i in range(len(T)):
        j = 0
        if (i == 1):
            Sol[i] = T[i]
        else:
            j = i - 1
            S1 = Sol[j]
            S2 = Sol[j - 1] + T[i]
            Sol[i] = max(S1, S2)
            if max(S1, S2) == S2 and S1 != S2:
                maison.append(i)
    return [maison, Sol[len(T) - 1]]


print(butinMax(T))
