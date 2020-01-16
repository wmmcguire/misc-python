import sqlite3

conn = sqlite3.connect('memberinfo.db')
c = conn.cursor() 


class User:
  __name = ""
  __height = 0
  __weight = 0
  __occupation = ""
  __workplace = ""
  
  def __init__(self, name, height, weight, occupation, workplace):
    self.__name = name
    self.__height = height
    self.__weight = weight
    self.__occupation = occupation
    self.__workplace = workplace
    
  def setName(self):
    self.__name = name
  
  def setHeight(self):
    self.__height = height
  
  def setWeight(self):
    self.__weight = weight
  
  def setOcc(self):
    self.__occupation = occupation
    
  def setWork(self):
    self.__workplace = workplace
    
  def getName(self):
    return self.__name 
  
  def getHeight(self):
    return self.__height
  
  def getWeight(self):
    return self.__weight
  
  def getOcc(self):
    return self.__occupation

  def getWork(self):
    return self.__workplace 
    
  def toString(self):
    return "{} is a {} at {}. {} tall and weighs {} pounds".format(self.__name, self.__occupation, self.__workplace, self.__height, self.__weight)

def mktb(table):
	makeTable = "CREATE TABLE %s(post_id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Height INTEGER, Weight INTEGER, Occupation TEXT, Workplace TEXT)" % table
	c.execute(makeTable)

	print("Table %s Created!\n" % table)

def addRow(name, height, weight, job, wkplace):
	tbName = input("Table Name: ")
	row = "INSERT INTO %s VALUES(?, ?, ?, ?, ?)" % tbName
	c.execute(row, (name, height, weight, job, wkplace))


def Main():

		while True:
			
			choice = int(input("Select and press Enter:\n1. Create Table\n2. Add Entry\n3. Remove Entry\n4. Exit\n"))

			if choice == 1:
				tb = input("Table Name: ")
				mktb(tb)
			elif choice == 2:
				name = input("Name: ")
				height = input("Height: ")
				weight = input("Weight: ")
				occupation = input("Job: ") 
				workplace = input("Workplace: ")
			else:
				break


			



if __name__ == '__main__':
	Main()


#babe = User("Kristina",66, 110, "IT Analyst", "Doctor.com") #enter data as directed when first calling function
#print(babe.toString())
    
    
  
  
  

