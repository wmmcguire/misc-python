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
	
	last = len(arr) - 1

	
	for i in range(0, last):
		sum1 = arr[i] + arr[i+1]
		if total == sum1:
			return "{} + {} = {}".format(arr[i], arr[i+1], total)



array1 = [2, 4, 6, 8, 10]
total = int(input('What is the total you are looking for? '))

print(arrMatch(total, array1))


