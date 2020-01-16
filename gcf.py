def gcf(num):

	gcf = []
	for x in range(1, num):
		if num % x == 0:
			gcf.append(x)
	return gcf


num1 = int(input("Give me a number and I'll tell you the GCFs: "))
print("The GCFs of ", num1, " are ", gcf(num1))