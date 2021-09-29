from math import *
from sys import *

k = int(eval(input()))
 
if (k == 0 or k == 1):
  print(k)
  exit()

i = 1
while (True):
    i *= 10
    x = k * (i - k) // (10 * k - 1)
    
    if (x * 10 + k) * k == k * i + x:
      break

print(x * 10 + k)

# Ak => 10x + k 

# kA = k * 10^n + x
# Ak * k = kA =>
# (10x + k) * k = k * 10^n + x
# 10xk + k^2 = k10^n + x
# 10xk - x = -k^2 + k10^n
# x(10k - 1) = k10^n - k^2 => k * (10^n - k)

# x = k * (10^n - k) / (10k - 1) <=