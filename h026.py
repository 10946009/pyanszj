def RPS(B,S):
    global drew, switch_count, round
    if (B == "2" and S == "5") or (B == "0" and S == "2") or (B == "5" and S == "0"):
        brother_list.append(B)
        drew = 0
        return 1
    elif B == S:
        round += 1
        switch_count += 1
        brother_list.append(B)
    else:
        brother_list.append(B)
        drew = 0
        return -1

def Switch(B):
    if    B == "0":   return "5"
    elif  B == "2":   return "0"
    else:             return "2"

drew = 1
round = 1
switch_count = 0
brother_list = []
brother = input()
sis_time = int(input())
sister = list(input().split())

for i in sister:
    result = RPS(brother, i)
    if result == 1:
        print(" ".join(brother_list), ": Won at round", round)
        break
    elif result == -1:
        print(" ".join(brother_list), ": Lost at round", round)
        break
    elif switch_count == 2:
        brother = Switch(brother)
        switch_count = 0

if drew == 1:
    print(" ".join(brother_list),": Drew at round", round-1)