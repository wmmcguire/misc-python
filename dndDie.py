import random 

amt = int(input('How many die are we rolling?: '))
sid = int(input('How many sides are the dice?:'))


rolls = []

for x in range(0, amt):
	die = random.randint(0, sid)
	rolls.append(die)

total = sum(rolls)
print("Your total is", total, ":", rolls)