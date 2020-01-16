'''
Word Search
by William McGuire
user enters a phrase with a folder in mind.
Computer will search for the word or phrase.
The file names where the word is found will be returned.
'''

import argparse

def search(word, dir):



def Main():

	parse = argparse.ArgumentParser()
	parse.add_argument("term" , help="The word that you are searching for.", type=str)
	parse.add_argument("dir" , help="The directory you are searching under. (i.e C:/Windows/)", type=str)
	args = parse.parse_args()

	directory = open(args.dir)

	for file in directory:
		

	else:

