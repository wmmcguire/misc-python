import string
import random

size = 10
lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = '0123456789'
syms = '@#$%^&!'

tpass = ''
for x in range(0, size - 3):
	tpass += random.choice(lower)
tpass += random.choice(upper) + random.choice(syms) + random.choice(nums)

print(tpass)
