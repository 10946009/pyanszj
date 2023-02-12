def f(a,b):
  if a % b == 0:
    return print(b)
  else:
    f(b,a%b)

a,b = map(int,input().split())
f(max(a,b),min(a,b))
