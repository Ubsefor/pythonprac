from math import *
from sys import *

number = int(input())
highest_power = floor(log(number, 2))
highest_number = floor(sqrt(number))

for i in range(2, highest_number):
  for j in range(2, highest_power):
    if i ** j == number:
      print("Digit: ", i, "Power: ", j)
      print("YES")
      exit()
            
print("NO")
