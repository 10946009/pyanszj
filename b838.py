R = 0
L = 0
t = int(input())
for i in range(t):
    n = input()
    for i in n:
        if R >= L:
            if i == '(':
                R += 1
            else:
                L += 1
        else:
            print("0")
            break
    if R == L:
        print(R)
    else:
        print(0)
    R = 0
    L = 0