##Temporary Password Script
#by William McGuire
#written on 08182019
#Script copies temporary password to clipboard
#For when end user forgets password

import random, argparse, string, pyperclip



def passwd(size):
	sz = size

	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	nums = '0123456789'
	syms = '@#$%^&!'
	
	tpass = ''
	for x in range(0, sz - 3):
		tpass += random.choice(lower)
	tpass += random.choice(upper) + random.choice(syms) + random.choice(nums)


	return tpass 


def Main():


	parse = argparse.ArgumentParser()
	parse.add_argument("-s", "--size", help="Desired password size.", type=int, default=8)
	args = parse.parse_args()

	#by default the password length will be 8 characters.
	pwSize = args.size
	pw = str(passwd(pwSize))
	pyperclip.copy(pw)
	print(pw + "\n..Copied to clipboard")


if __name__ == "__main__" :
	Main()




