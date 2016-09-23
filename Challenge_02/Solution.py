inputs = open("input.txt", "r").readlines()		# We put the content of input.txt in a variabe
paper = 0										# Start area of paper (feet squared)
ribbon = 0										# Start length of ribbon (feet)
for i in inputs:								# We go through eery line of the input (so every figt)
	i = [int(x) for x in i.split('x')]			# We transform the ??x??x?? string into an array of 3 integers
												# We apply some math magic
												#	paper  -> calculate area and add area of the smallest face
												#	ribbon -> Area of the 2 shortest distance around the face
												#	 		  where we add special (volume) formula of the bow
	paper += 2*i[0]*i[1] + 2*i[1]*i[2] + 2*i[2]*i[0]  + min(i[2]*i[0], i[2]*i[1], i[1]*i[0])
	ribbon += 2*(sorted(i)[0] + sorted(i)[1]) + i[2]*i[1]*i[0]

print("They should order " + str(paper) + " square feet of wrapping paper.")
print("They should order " + str(ribbon) + " feet of ribbon.")
