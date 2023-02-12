while True:
    try:
        a = input()
        n = 1
        t = ''
        b = 0
        for i in range(1, len(a)):
            if a[i-1] == a[i]:
                n += 1
                if n > b:
                    b = n
                    t = a[i-1]
            else:
                n = 1
        print(t, b)
    except:
        break
