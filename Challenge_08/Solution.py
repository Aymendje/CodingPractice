import ast, re
inputs = open("input.txt", 'r').read().splitlines()
delta1 = 0
delta2 = 0
for i in inputs:
	real = len(i)
	mem = len(ast.literal_eval(i))
	esc = len(re.escape(i)) + 2
	delta1 += real - mem
	delta2 += esc - real
print(delta1)
print(delta2)
