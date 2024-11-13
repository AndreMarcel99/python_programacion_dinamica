def main():

    length = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    price = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]

    results = [0 for i in range(len(length))]

    cuts = [1 for i in range(len(length) + 1)]

    for j in range(1, len(length)):
        q = -100
        for i in range(1, j + 1):
            if q < price[i - 1] + results[j - i]:
                cuts[j] = i
            q = max(q, price[i - 1] + results[j - i])
        results[j] = q


    for i in range(len(length)):
        print(length[i], results[i])
        n = length[i]
        while (n > 0):
            print(cuts[n])
            n =  n - cuts[n]

main()