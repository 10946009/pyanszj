l = []
time = int(input())
for i in range(time):
    num = input()
    if num[0] == "1":
        l.append(int(num[2]))
    elif num[0] == "2":
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
    elif num[0] == "3":
        if len(l) != 0:
            l.pop(0)

#NA