while True:
    try:
        a = int(input())
        a = str(bin(a))
        a = a[2:]
        print(a)
        
    except:
        break