while 1:
    l = []
    String = input()
    if String == "END":
        break
    else:
        String = String.split(" ")
        for i in range(len(String)):
            l.append(String[i][0].upper())
        print("".join(l), String[len(String)-1])