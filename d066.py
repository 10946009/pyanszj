hh, mm = input().split(" ")
if mm[0] == "0":
    mm = int(mm[1]) 
else:
    mm = int(mm)
hh = int(hh)
if hh == 7 and mm >= 30:
    print("At School")
elif 7 < hh < 17:
    print("At School")
else:
    print("Off School")
        