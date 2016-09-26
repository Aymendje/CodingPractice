import itertools

inputs = open("input.txt").readlines()
distances = {}
places = set()
for line in inputs:
	line = line.strip().split(' ')
	places.add(line[0])
	places.add(line[2])
	distances[(line[2], line[0])] = int(line[-1])
	distances[(line[0], line[2])] = int(line[-1])

max_v = [None, ['']]
min_v = [None, ['']]

for subset in itertools.permutations(places, len(places)):
	current = 0
	for i in range(len(subset)-1):
		current += distances[(subset[i], subset[i+1])]

	if max_v[0] is None or max_v[0] < current:
		max_v[0] = current
		max_v[1] = subset
		
	if min_v[0] is None or min_v[0] > current:
		min_v[0] = current
		min_v[1] = subset
		
print(" -> ".join(min_v[1]) + " = " + str(min_v[0]))
print(" -> ".join(max_v[1]) + " = " + str(max_v[0]))
