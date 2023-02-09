while True:
    try:
        a = input().replace("/", "//")
        print(eval(a))
    except:
        break