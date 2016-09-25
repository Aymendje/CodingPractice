import re
inputs = open("input.txt", 'r').read().splitlines()

grid = [x[:] for x in [[False]*1000]*1000]

for lines in inputs:
	lines = lines.split(" ")

	if lines[0] == "turn":
		lines.pop(0)

	x_start = int(lines[1].split(',')[0])
	y_start = int(lines[1].split(',')[1])

	x_end = int(lines[3].split(',')[0])
	y_end = int(lines[3].split(',')[1]) 


	if lines[0] == "toggle":
		for x in range(x_start, x_end + 1):
			for y in range(y_start, y_end + 1):
				grid[y][x] = not grid[y][x]
	else:
		if lines[0] == "on":
			value = True
		else:
			value = False
		for x in range(x_start, x_end + 1):
			for y in range(y_start, y_end + 1):
				grid[y][x] = value

lit = 0
for x in range(1000):
	for y in range(1000):
		if (grid[y][x]):
			lit += 1
print(lit)



grid = [x[:] for x in [[0]*1000]*1000]
for lines in inputs:
	lines = lines.split(" ")

	if lines[0] == "turn":
		lines.pop(0)

	x_start = int(lines[1].split(',')[0])
	y_start = int(lines[1].split(',')[1])

	x_end = int(lines[3].split(',')[0])
	y_end = int(lines[3].split(',')[1]) 

	value = 0
	if lines[0] == "toggle":
		value = 2
	elif lines[0] == "on":
		value = 1
	else:
		value = -1

	for x in range(x_start, x_end + 1):
		for y in range(y_start, y_end + 1):
			grid[y][x] = max(value + grid[y][x], 0)

lit = 0
for x in range(1000):
	for y in range(1000):
		if (grid[y][x]):
			lit += grid[y][x]
print(lit)
