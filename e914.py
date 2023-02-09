result = []
possible = [[2, 20], [12, 21], [3, 30], [13, 31], [23, 32], [4, 40], [14, 41], [24, 42], [34, 43], [5, 50], [15, 51], [25, 52], [35, 53], [45, 54], [6, 60], [16, 61], [26, 62], [36, 63], [46, 64], [56, 65], [7, 70], [17, 71], [27, 72], [37, 73], [47, 74], [57, 75], [67, 76], [8, 80], [18, 81], [28, 82], [38, 83], [48, 84], [58, 85], [68, 86], [78, 87], [9, 90], [19, 91], [29, 92], [39, 93], [49, 94], [59, 95], [69, 96], [79, 97], [89, 98]]
n = int(input())
#for i in range(18, 100):
#    Mom = i
#    daughtor = "".join(reversed(str(i)))
#    if daughtor[0] == 0:
#        daughtor = int(daughtor[1])
#    else:
#        daughtor = int(daughtor)
#    if Mom > daughtor:
#        possible.append([daughtor, Mom])
for i in possible:
    if 2*(i[0] + n) == i[1] + n and i[1] + n <= 99:
        result.append(str(i[0]))
if len(result) == 0:
    print("no answer")
else:
    print(" ".join(result))
