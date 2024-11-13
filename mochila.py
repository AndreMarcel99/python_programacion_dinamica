def main():

    n = 10
    w = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
    v = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
    W = 140

    V = [[0 for column in range(0, W + 1)]    for row in range(0, n + 1)]

    for i in range(1, n + 1):
        for x in range(0, W + 1):
            j = x - w[i - 1]
            if j < 0:
                V[i][x] = max(V[i-1][x], 0)
            else:
                V[i][x] = max(V[i-1][x], V[i-1][j] + v[i - 1])

    print(V[n][W])

    selected_items = []

    s = W

    for i in range(n, 0, -1):
        if V[i][s] != V[i-1][s]:
            selected_items.append(i) # i - 1 iniciando cuenta en 0
            s -= w[i-1]

    selected_items.reverse()

    print(selected_items)

main()