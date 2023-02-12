while True:
    try:
        num=int(input())
        num_list=list(map(int,input().split()))
        num_list.sort(key=lambda z:(z%10,-z))
        print(*num_list)
         
         
    except:
        break
