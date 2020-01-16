# Object-Oriented Programming practice with Python

class Element:

	__name = ''
	__abbr = ''
	__aNum = 0
	__aMass = 0
	__group = ''



	def __init__(self, name, abbr, aNum, aMass, group):

		self.__name = name
		self.__abbr = abbr
		self.__aNum = aNum
		self.__aMass = aMass
		self.__group = group

	def setName(self): #setters
		self.__name = name
	def setAbbr(self):
		self.__abbr = abbr
	def setaNum(self):
		self.__aNum = aNum
	def setaMass(self):
		self.__aMass = aMass
	def setGroup(self):
		self.__group = group

	def getName(self):  #getters
		return self.__name
	def getAbbr(self): 
		return self.__abbr
	def getaNum(self): 
		return self.__aNum
	def getaMass(self): 
		return self.__aMass
	def getGroup(self):
		return self.__group

	def toString(self):
		return "{}, or {}, is number {} on the periodic table.\nIts atomic mass is {}.\nIt is part of group {}.\n\n".format(self.__name, self.__abbr, self.__aNum, self.__aMass, self.__group)


pdcTable = []

H = Element('Hydrogen', 'H', 1, 1.008, 'N/A')
O = Element('Oxygen', 'O', 8, 16, 'Non-Metal')

pdcTable.append(H)
pdcTable.append(O)

for i in range(0, len(pdcTable)):
	print(pdcTable[i].toString())




