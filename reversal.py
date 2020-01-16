class Reverse:

	def __init__(self, data):
		self.__data = data
		self.__index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.__index == 0: # when there are no chars left
			raise StopIteration
		self.__index = self.__index - 1
		return self.__data[self.__index]

def Main():
	rev = Reverse('I am the fastest man alive')

	thawne = ''


	for char in rev:
		thawne += char
		print(thawne)


if __name__ == '__main__':
	Main()

