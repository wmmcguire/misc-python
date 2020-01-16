import random


def sort(arr):
	while True:
		corrected = False #tells prog whether correction has been made
		for i in range(0, len(arr)- 1): #iterate on second to last item, compare with last item
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				corrected = True
		if not corrected:
				return arr

array = []
amt = int(input('Enter amount of terms to add to array: '))
choice = int(input('Enter numbers at 1)random, or 2)manually?: '))



if choice == 1: # generate random numbers and then sort them
	for x in range(0, amt):
		num = array.append(random.randrange(0,15))
	print('Your array is: ', array)

	sort = sort(array)

	print('The sorted array: ', sort)



else: # enter your own numbers
	
	
	for x in range (0, amt):
		num = array.append(int(input('Enter a number: ')))

	print('Your array is: ', array)

	sort = sort(array)

	print('The sorted array: ', sort)

