def Prime(n):
    if n == 1:
        return True
    elif (n % 2 == 0):
        return Prime(n//2)
    elif (n % 3 == 0):
        return Prime(n//3)
    elif (n % 5 == 0):
        return Prime(n//5)
    else:
        return False

print("Start")
num = 1
count = 0
while 1:
    if Prime(num) == True:
        count += 1
        if count == 1500:
            print(num)
            break
    num += 1
    print("count: ", count)




# too slow!