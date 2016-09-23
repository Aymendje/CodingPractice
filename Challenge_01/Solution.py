input = open("input.txt", "r").read()		# We put the content of input.txt in a variabe
floor = 0									# Start floor
first_low = None 							# First floor lower than 0 (2nd part of question)
for i in range(len(input)):					# We loop through every character inside the input
	if input[i] == '(':						# If we see (, we go up
		floor += 1
	elif input[i] == ')':					# else, if we see ), we go down
		floor -= 1
	if first_low == None and floor < 0:		# If we have never been to a negative floor, AND
		first_low = i + 1					# the current floor is a negative one, we save it (i starts at 0, so we add one)

print("The instructions take Santa to the " +str(floor) + ".")
print("The position of the character that causes Santa to first enter the basement is " + str(first_low) + ".")