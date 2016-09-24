def move(d, position):
	if d == '>':
		position[0] += 1
	elif d == '<':
		position[0] -= 1
	elif d == '^':
		position[1] += 1
	elif d == 'v':
		position[1] -= 1
	return position


inputs = open("input.txt", 'r').read()
position = [0, 0]
visited = set([str(position[0])+','+str(position[1])])
for d in inputs:
	position = move(d, position)
	visited.add(str(position[0])+','+str(position[1]))
print("Last year, Santa delivered a least " + str(len(visited)) + " presents !")


position = [0, 0]
rposition = [0, 0]
visited = set([str(position[0])+','+str(position[1])])
for i in range(0, len(inputs), 2):
	position = move(inputs[i], position)
	visited.add(str(position[0])+','+str(position[1]))
	if(i+1 < len(inputs)):
		rposition = move(inputs[i+1], rposition)
		visited.add(str(rposition[0])+','+str(rposition[1]))
print("This year, Santa and Robo-Santa delivered a least " + str(len(visited)) + " presents !")