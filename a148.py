while 1:
    try:
        n = list(map(int, input().split()))
        l = len(n)-1
        n = sum(n[1:])
        if n / l > 59:
            print("no")
        else:
            print("yes")
    except:
        break