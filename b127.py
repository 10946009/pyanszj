# def f(a):
#     if a == 0 or a == 1:
#         return a
#     return f(a-1) + f(a-2)
#

f =[1, 1]
while True:
    try:
        for i in range(2, 46):
            f.append(f[i-1] + f[i-2])
        a = int(input())
        print(f[a])
    except:
        break