#create own function
import string 
import random



amt = int(input('How many letters in the name?: '))

name = ''
  
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
lowers = string.ascii_lowercase
  
for x in range(0, amt):
  letter = input('Input a letter: v for vowel, c for consonant, l for any letter:')
  if len(letter) > 1:
  	print("You must enter ONLY one letter.")
  	exit()
  elif letter == "v":
    name += random.choice(vowels)
  elif letter == "c":
    name += random.choice(consonants)
  elif letter == "l":
    name += random.choice(lowers)
  else:
    name += letter
    
capName = name.upper() 
propName = capName[0] + name[1:] # i.e "B" + "illy"

  
print("Your baby's new name is", propName)

input("Press enter to exit.")
  
  

