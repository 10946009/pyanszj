while True:
    try:
        S = ""
        matrix = []
        row, column = map(int, input().split())

        for i in range(row):
            matrix.append(list(map(int, input().split())))

        for i in range(column):
            for j in range(row):
                S += str(matrix[j][i]) + " "
            print(S[0:-1])
            S = ""
    except:
        break