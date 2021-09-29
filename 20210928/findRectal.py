#!/usr/bin/env python

buf = ''
field = []
buf = input()
flag = 0
count = 0

while buf[0] != '-' or flag == 0:
	field.append(buf)
	buf = input()
	flag += 1

# *y
# x
	
x_length = field[0].__len__() - 1
y_length = field.__len__()
for i in range(1, x_length):
	for j in range(0, y_length):
		if (
			field[j][i] == '#' and \
			(field[j - 1][i] == '-' or field[j - 1][i] == '.') and \
			(field[j][i - 1] == '-' or field[j][i - 1] == '.') and \
			(field[j - 1][i - 1] == '-' or field[j - 1][i - 1] == '.') \
			): # detect corners, cause due to the task this is enough
			count += 1
		
print(count)