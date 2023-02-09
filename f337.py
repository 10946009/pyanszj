n, m = map(int, input().split())
n2 = n * 2
n3 = n * 3
m  = 8 * m
if n2 <= m and n3 >= m:
    print("Yes")
elif n2 > m:
    print("Not enough")
elif n2 < m and n3 < m:
    print("Too much")
