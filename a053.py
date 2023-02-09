score = int(input())
if score > 10:
    if score > 20:
        if score >= 40:
            print(100)
        else:
            print(80 + (score-20))
    else:
        print(60+(score-10)*2)
else:
    print(score*6)