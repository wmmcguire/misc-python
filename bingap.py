import string

def binGap(N):

	binstr = str(bin(N)) # convert number to string
	binary = binstr[2:] #0b|xxxxxxxx
	

	bingaps = []
	zcnt = 0

	for bit in binary:
		if bit != '1':
			zcnt += 1 #count characters that aren't 1, which are zeroes in this case.
		else:
			bingaps.append(zcnt) #append the counted binary gap into the array
			zcnt = 0 # reset the counter
			#when statement finds a 1, it will add onto the array.
	return max(bingaps)

decNum = int(input('Enter a decimal integer: '))
print("You have entered the number "+str(decNum)+ ", "+bin(decNum)+".")

maxGap = binGap(decNum)

print('Biggest binary gap is '+str(maxGap)+'.')

