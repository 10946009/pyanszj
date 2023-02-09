Dic = {}
rocks = input().split()
for i in rocks:
    if i in Dic:
        Dic[i] += 1
    else:
        Dic[i] = 1
for i in Dic:
    if Dic.get(i) % 3 != 0:
        print(i)
        break