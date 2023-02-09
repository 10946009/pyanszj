a, b = map(int, input().split())
if a == 1 or b == 1:
    print(1)
elif a == b:
    print(a)
else:
    result = 0
    if a > b:
        a, b = b, a
    for i in range(2, b+1):
        if a % i == 0 and b % i == 0:
            result = i
    print(result)

#TLE