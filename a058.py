l = []
mod = 0
mod1 = 0
mod2 = 0
time = int(input())
for i in range(time):
    num = int(input())
    l.append(num)
for i in l:
    if i % 3 == 0:
        mod += 1
    if i % 3 == 1:
        mod1 += 1
    if i % 3 == 2:
        mod2 += 1
print(mod, mod1, mod2)