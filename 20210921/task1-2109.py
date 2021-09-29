x = eval(input())
center = x[0:2]
radius = x[2]
x = eval(input())
while (x != (0,0)):
  if ((((center[0] - x[0]) ** 2 + (center[1] - x[1]) ** 2) ** 0.5) > radius): 
    print("NO")
    break
  x = eval(input())
else:
  print("YES")