def print_optimal_parenthesis(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parenthesis(s, i, s[i][j])
        print_optimal_parenthesis(s, s[i][j] + 1, j)
        print(")", end="")

def main():

    p = [5,10,3,12,5,50,6]

    n = len(p) - 1

    m = [[0 for column in range(0, n)]    for row in range(0, n)]
    s = [[0 for column in range(0, n)]    for row in range(0, n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float("inf")

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + (p[i] * p[k + 1] * p[j + 1])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print(m[0][n - 1])

    print_optimal_parenthesis(s, 0, len(p)-2)



main()