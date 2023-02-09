length = int(input())
String = list(input())

while 1:
    try:
        S = ""
        L, R = map(int, input().split())
        for i in range(L-1,R):
            S += String[i]
        print(S)
        S = ""
    except:
        break