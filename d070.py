l = []
while 1:
    y = int(input())
    if y == 0:
        break
    else:
        l.append(y)

for i in l:
    if i % 100 == 0 and i % 400 == 0:
        print("a leap year")
    elif i % 4 == 0 and i % 100 != 0:
        print("a leap year")
    else:
        print("a normal year")