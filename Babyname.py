#create own function
import string 
import random



letters = []
  
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
lowers = string.ascii_lowercase
  
for x in range(0,5):
  enter = input('Input a letter: v for vowel, c for consonant, l for any letter:')
  if enter == "v":
    letters.append(random.choice(vowels))
  elif enter == "c":
    letters.append(random.choice(consonants))
  elif enter == "l":
    letters.append(random.choice(lowers))
  else:
    letters.append(enter)
    
name = letters[0:]
  
print(name)

endprog = input("Press enter to exit.")
  
  

