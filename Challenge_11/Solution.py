import re

inputs = open("input.txt").read().strip()

c1 = r"^.*("+ r'|'.join([chr(i)+chr(i+1)+chr(i+2) for i in range(ord('a'), ord('z')-1, 1)]) + r")+.*$"
c2 = r"^[^iol]+$"
c3 = r"^.*(" + r'|'.join([chr(i)+chr(i) for i in range(ord('a'), ord('z')+1, 1)]) + r")+.*(" + r'|'.join([chr(i)+chr(i) for i in range(ord('a'), ord('z')+1, 1)]) + r")+.*$"

r1 = re.compile(c1, re.IGNORECASE)
r2 = re.compile(c2, re.IGNORECASE)
r3 = re.compile(c3, re.IGNORECASE)

def incrementString(s):
	if s == 'zzzzzzzz':
		return 'aaaaaaaa'
	s = [x for x in s]
	for i in range(len(s)-1, -1, -1):
		if s[i] == 'z':
			s[i] = 'a'
		else:
			s[i] = chr(ord(s[i]) + 1)
			return ''.join(s)


def checkString(s):
	if ((r1.match(s) is not None) and \
		(r2.match(s) is not None) and \
		(r3.match(s) is not None)):
		return True
	else:
		return False


password = incrementString(inputs)
while(checkString(password) != True):
	password = incrementString(password)
print(password)

password = incrementString(password)
while(checkString(password) != True):
	password = incrementString(password)
print(password)