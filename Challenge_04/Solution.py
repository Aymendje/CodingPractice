import hashlib
i = 0
inputs = open("input.txt", "r").read().strip()
while True:
	if hashlib.md5((inputs+str(i)).encode("ascii")).hexdigest()[0:5] == "00000" :
		print(str(i))
		break
	i += 1
	
while True:
	if hashlib.md5((inputs+str(i)).encode("ascii")).hexdigest()[0:6] == "000000":
		print(str(i))
		break
	i += 1
