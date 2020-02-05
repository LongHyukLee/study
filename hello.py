tmp = [[i*5 +j for j in range(1, 6)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        print(tmp[i][j], end = ' ')
    print()

    