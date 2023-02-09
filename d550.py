l = []
N, M = map(int, input().split())
for i in range(N):
    l.append(list(map(int, input().split())))
l.sort()
for i in l:
    i = map(str, i)
    print(" ".join(i))