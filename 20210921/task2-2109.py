x = eval(input())
y = x
a = 0

if x % 10 != 0 :
  while (x != 0):
    a = a * 10 + x % 10
    x = x // 10
  if a == y: print("YES")
  else: print("NO")
else:
  print("NO")