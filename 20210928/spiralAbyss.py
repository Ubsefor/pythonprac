#!/usr/bin/env python

m, n = [int(i) for i in input().split(',')]

lst = []
for i in range(0, m):
	lst.append([]);
	for j in range(0, n):
		lst[i].append(-1)
		
direction = 0
y = 0
x = 0

#  y->
# x * -> *
# V A    V
#   A    V
#   * <- *
#
for i in range(0, m * n):
	if lst[y][x] == -1:
		lst[y][x] = i % 10
		
	if direction % 4 == 0:
		if y + 1 > m - 1 or lst[y + 1][x] != -1:
			direction += 1 # change direction
			x += 1
		else:
			y += 1
	elif direction % 4 == 1:
		if x + 1 > n - 1 or lst[y][x + 1] != -1:
			direction += 1 # change direction
			y -= 1
		else:
			x += 1
	elif direction % 4 == 2:
		if y - 1 < 0 or lst[y - 1][x] != -1:
			direction += 1 # change direction
			x -= 1
		else:
			y -= 1
	elif direction % 4 == 3:
		if x - 1 < 0 or lst[y][x - 1] != -1:
			direction += 1 # change direction
			y += 1
		else:
			x -= 1 
			
for i in range(0, n):
	for j in range(0, m):
		print(lst[j][i], ' ', end='')
	print()