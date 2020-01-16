import random
import argparse


def sort(arr):
	while True:
		corrected = False #tells prog whether correction has been made
		for i in range(0, len(arr)- 1): #iterate on second to last item, compare with last item
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				corrected = True
		if not corrected:
				return arr

def Main():
	array = []


	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-r", "--random", action="store_true")
	# group.add_argument("-s", "--select", action="store_true")
	parser.add_argument("amt", help="How many numbers you want to sort.", type=int, action="store_const")
	parser.add_argument("-o", "--output", help="Output result to file.", action="store_true")

	args = parser.parse_args()

	amt = args.amt


	if args.random: # generate random numbers and then sort them
		for x in range(0, amt):
			num = array.append(random.randrange(0,100))
		print('Your array is: ', array)

		result = sort(array)

		print('The sorted array: ', result)



	else: # enter your own numbers
		
		
		for x in range (0, amt):
			num = array.append(int(input('Enter a number: ')))

		print('Your array is: ', array)

		result = sort(array)

		print('The sorted array: ', result)

	if args.output:
		a = open("bubsort.txt", "a")
		a.write(str(result)+'\n')

if __name__ == "__main__":
	Main()
