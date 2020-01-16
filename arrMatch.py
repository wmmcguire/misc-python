def sort(arr1):
	while True:
		corrected = False #tells prog whether correction has been made
		for i in range(0, len(arr1)- 1): #iterate on second to last item, compare with last item
			if arr1[i] > arr1[i+1]:
				arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
				corrected = True
		if not corrected:
				return arr1


def arrMatch(total, arr):
	
	gcf = []

	
	for i in range(0, len(arr) - 1):
		if total % arr[i] == 0: # if element fits evenly into total
			gcf.append(arr[i])
	print('Your GCFs are: ', gcf)
	lastNum = len(gcf) - 1 # last value in the array	
	for j in range(0, len(gcf) - 1):
		sum1 = gcf[j] + gcf[lastNum]
		if total == sum1: #compare j term + last term
			return "{} + {} = {}".format(gcf[j], gcf[lastNum], total)
			


array1 = [2, 4, 6, 8, 10]
total = int(input('What is the total you are looking for? '))

print(arrMatch(total, array1))


