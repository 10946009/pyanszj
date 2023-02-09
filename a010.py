num = int(input())
ans = ""
for i in range(2, num+1):
    flag = 0
    while num % i == 0:
        num = num / i
        flag += 1
    if flag > 1:
        ans += str(i) + "^" + str(flag)
        if num > 1: 
            ans += " * "
    elif flag == 1:
        ans += str(i)
        if num > 1:
            ans += " * "
print(ans)