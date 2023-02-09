Sum = 0
day = int(input())
each = list(map(int, input().split(" ")))

for i in range(len(each)):
    Sum += each[i] * (i+1)
print(Sum)