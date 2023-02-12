a=list(input())
first_eng=ord(a[0])-55
if first_eng ==18:
  first_eng=34
elif first_eng==24:
  first_eng=35
elif first_eng==33:
  first_eng=30
elif first_eng==32:
  first_eng=32
elif first_eng==34:
  first_eng=31
elif first_eng==35:
  first_eng=33
elif first_eng>24:
  first_eng-=2
elif first_eng>18:
  first_eng-=1
j=8
a020=0
for i in range(1,9):
  a020+=int(a[i])*j
  j-=1
a020+=(first_eng//10)+(first_eng%10)*9+int(a[9])
if a020%10==0:
  print("real")
else:
  print("fake")
