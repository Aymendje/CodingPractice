import re
inputs = open("input.txt", 'r').read().splitlines()

redo = True
def doCircuit(override=0):
	circuit = {}
	redo = True
	while redo:
		redo = False
		for line in inputs:
			line = line.split()
			if override > 0 and line[-1] == 'b':
				circuit[line[-1]] = override
			else:
				if line[0] == "NOT":
					try:
						circuit[line[-1]] = ~circuit[line[1]]
					except:
						redo = True
						continue
				else:
					value1 = 0
					try:
						value1 = int(line[0])
					except:
						try:
							value1 = circuit[line[0]]
						except:
							redo = True
							continue

					if line[1] == "->":
						circuit[line[-1]] = value1
					else:
						try:
							value2 = int(line[2])
						except:
							try:
								value2 = circuit[line[2]]
							except:
								redo = True
								continue

						if line[1] == "AND":
							circuit[line[-1]] = value1 & value2
						elif line[1] == "OR":
							circuit[line[-1]] = value1 | value2
						elif line[1] == "LSHIFT":
							circuit[line[-1]] = value1 << value2
						elif line[1] == "RSHIFT":
							circuit[line[-1]] = value1 >> value2
	return circuit['a'] & 0xffff
a = doCircuit()

print(a)
print(doCircuit(a))
