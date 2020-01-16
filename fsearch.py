from re import search
import argparse

def Main():
	parser.add_argument('word', help='specify word to search for')
	parser.add_argument('name', help='file to search')
	args = parser.parse_args


	search = open(args.name)
	lineNum=0

	for line in search.readlines():
		line = line.strip('\n\r')
		lineNum += 1
		schResult = re.search(args.word, line, re.M|re.I)

		if schResult:
			print(str(lineNum)+': '+line)