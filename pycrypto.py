

#this program uses Advanced Encryption Standard, or AES
# - Symmetric Cipher
# - 16-byte block size(128 bits)
# - Keys can be 128, 192, or 256 bits long
# - Many block cipher modes. See wikipedia.
# - Cryptography - encrypting plain text into ciphertext

# IV - initialization vector
# Used to randomize and produce distinct ciphertexts for certain modes
# Don't reuse the same IV
# IV can be known for most modes
# 
# 
# 
# We'll practice using a file encryptor by Draps.
# 



import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes 
import argparse 

def encrypt(key, filename):
	chunksize = 64*1024
	outputFl = "(encrypted)"+filename

	filesize = str(os.path.getsize(filename)).zfill(16) #make sure it fits

	IV = Random.new().read(16) #read 16 bytes out of a random IV

	encryptor = AES.new(key, AES.MOSE_CBC, IV)
	#pass the key into AES

	with open(filename, 'rb') as infile: #rb = read binary
		with open(outputFl, 'wb') as outfile: #wb = write binary
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 !=0: # adds padding
					chunk += b' ' * (len(chunk) % 16)
					# space into byte form, times the length of the chunk mod 16

				outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
	chunksize = 64*1024
	outputFl = filename[11:]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFl, 'wb') as outfile: #wb = write binary
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize) # gets rid of padding from encryption stage

def getKey(passwd):
	hasher = SHA256.new(passwd.encode('utf-8'))
	return hasher.digest()



def Main():
	
	prs = argparse.ArgumentParser()
	grp = prs.add_mutually_exclusive_group()
	grp.add_argument('-e', "--encrypt", help="Encrypt the file.", action="store_true")
	grp.add_argument('-d', "--decrypt", help="Decrypt the file.", action="store_true")
	prs.add_argument("filename", help="Name of the file you'd like to encrypt.", type=str)


	arg = prs.parse_args()
	


	if arg.encrypt:
		
		filename = arg.filename
		passwd = input("Password: ")

		encrypt(getKey(passwd, filename))
		print("..Done.")

	elif arg.decrypt:
		filename = input("File to decrypt: ")
		passwd = input("Password: ")
		decrypt(getKey(passwd, filename))
		print("..Done.")

	else: 
		choice = input("would you like to (E)ncrypt or (D)ecrypt?: ")

		if choice == 'E' or choice == 'e':
			filename = input("File to encrypt: ")
			passwd = input("Password: ")
			encrypt(getKey(passwd, filename))
			print("..Done.")

		elif choice == 'D' or choice == 'd':
			filename = input("File to encrypt: ")
			passwd = input("Password: ")
			encrypt(getKey(passwd, filename))
			print("..Done.")





if __name__ == '__main__':
	Main()


