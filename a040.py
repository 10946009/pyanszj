Ans = []
Sum = 0
n, m = map(int, input().split(" "))
for i in range(n, m+1):
    time = len(str(i))
    for j in str(i):
        Sum += int(j)**time
    if Sum == i:
        Ans.append(str(i))
    Sum = 0
if len(Ans) == 0:
    print("none")
else:
    print(" ".join(Ans))