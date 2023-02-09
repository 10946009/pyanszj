import math                                                                                              

def is_sqr(n):
    a = int(math.sqrt(n))
    return a * a == n

L = []
time = int(input())
for i in range(time):
    Min = int(input())
    Max = int(input())
    L.append([Min, Max])
Sum = 0
for i in range(len(L)):
    for j in range(L[i][0], L[i][1]+1):
        if (is_sqr(j)):
            Sum += j
    print("Case "+str(i+1)+":", Sum)
    Sum = 0