n = input()
a = list(map(int, input().split()))
a = sorted(list(set(a)))
print(len(a))
print(' '.join(map(str, a)))