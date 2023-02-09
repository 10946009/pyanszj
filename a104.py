while 1:
    try:
        time = int(input())
        print(" ".join(list(map(str, sorted(list(map(int, input().split())))))))
    except:
        break