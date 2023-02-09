def Add_old_list(S_List, num):
    for i in S_List:
        if num in i:
            i.append(num)
while 1:
    try:
        same_list = []
        men = int(input())
        men_list = list(map(int, input().split()))
        for i in range(len(men_list)):
            if men_list[i] != 0:
                if men_list[men_list[i]-1] != 0:
                    same_list.append([men_list[i], men_list[men_list[i]-1]])
                    men_list[i] = 0
                    men_list[men_list[i]-1] = 0
                else:
                    Add_old_list(same_list, i)
                    men_list[i] = 0
        print(same_list)
        print(len(same_list))
        print(len(max(same_list)))
    except EOFError:
        break



a = []
a.append([1,2])
print(a)