inputs = open("input.txt").readlines()

people = set()
happyness = {}
for i in range(len(inputs)):
	inputs[i] = inputs[i].split(' ')
	happy = int(inputs[i][3])
	if inputs[i][2] == 'lose':
		happy *= -1
	happyness[inputs[i][0]+'_'+inputs[i][-1].strip()[:-1]] = happy
	people.add(inputs[i][0])
people = list(people)

def calc():
	import itertools
	maximum = 0
	possible = itertools.permutations(people)
	possible = [i for i in possible]
	for table in possible:
		happy = 0
		for person in range(len(table) - 1):
			happy += happyness[table[person]+'_'+table[person+1]]
		happy += happyness[table[-1]+'_'+table[0]]

		for person in range(len(table)-1, 0, -1):
			happy += happyness[table[person]+'_'+table[person-1]]
		happy += happyness[table[0]+'_'+table[-1]]
		if maximum < happy:
			maximum = happy
	return maximum

print(calc())

for i in people:
	happyness["Me_"+i] = 0
	happyness[i+"_Me"] = 0
people.append("Me")
print(calc())