#!/usr/bin/env python

x = list(eval(input()))
x.sort(key=lambda tup:(tup[0]))
y = 0; # summ

lxs = x[0][0]
rxs = x[0][1]

for i in range(0, x.__len__() - 1):
	if x[i+1][0] <= rxs:
		if x[i+1][1] >= rxs:
			rxs = x[i+1][1]
	else:
		y += (rxs - lxs)
		lxs = x[i+1][0]
		rxs = x[i+1][1]

y += (rxs - lxs)
print(y)
		