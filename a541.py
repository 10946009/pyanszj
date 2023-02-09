know = []
know_time = int(input())
for i in range(know_time):
    know.append(input())
find_time = int(input())
for i in range(find_time):
    name = input()
    if name in know:
        print("yes")
    elif name not in know:
        print("no")
        know.append(name)




#        1%    NA