import re
inputs = open("inputs.txt", 'r').read().splitlines()


r1 = re.compile(r"^.*[aeiou].*[aeiou].*[aeiou].*$", re.IGNORECASE)
r2 = re.compile(r"^.*(.)\1.*$", re.IGNORECASE)
r3 = re.compile(r"^((?!ab|cd|pq|xy).)*$", re.IGNORECASE)

nice = 0
for i in inputs:
	if ((r1.match(i) is not None) and \
		(r2.match(i) is not None) and \
		(r3.match(i) is not None)):
		nice += 1
print (nice)


r1 = re.compile(r"^.*(..).*\1.*$", re.IGNORECASE)
r2 = re.compile(r"^.*(.).\1.*$", re.IGNORECASE)
nice = 0
for i in inputs:
	if ((r1.match(i) is not None) and \
		(r2.match(i) is not None)):
		nice += 1
print (nice)
