a = int(input())
b=2
if a==1:
  print(1)
elif a>=2:
  while a>=b:
    c=1
    if a%b==0 and a!=1:
      print(b,end='')
      a/=b
      if a%b==0 and a!=1:
        while(a%b==0 and a!=1):
          c+=1
          a/=b
        print(f"^{c}",end='')
      if a!=1:
        print(" * ",end='')
    b+=1
else:
  print(0)
