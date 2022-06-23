from inspect import iscode
import sys
import shutil

helpCase = ["help", "h"]

isCodeBlock = 0

class Color:
	BLACK		=	'\033[30m'
	RED			=	'\033[31m'
	GREEN		=	'\033[32m'
	YELLOW		=	'\033[33m'
	BLUE		=	'\033[34m'
	PURPLE		=	'\033[35m'
	CYAN		=	'\033[36m'
	WHITE		=	'\033[37m'
	END			=	'\033[0m'
	BOLD		=	'\038[1m'
	UNDERLINE	=	'\033[4m'
	INVISIBLE	=	'\033[08m'
	REVERCE		=	'\033[07m'

def usage():
	print("""
+------------------------------------------+
| Usage:                                   |
|    > python3 main.py <ReadmeFileName>.md |
+------------------------------------------+
""")

def checkArg(args):
	if (args[1][-3:] == ".md"):
		return True
	elif (args[1] in helpCase):
		usage()
	return False

def errorHub(n):
	printUsageCase = [1, 2]

	print("Error" + str(n) + " : ", end="")
	if (n == 1):
		print("Invalid number of Armument.")
	if (n == 2):
		print("Invalid file.")
	if (n in printUsageCase):
		usage()

def getDataSet(fileName):
	f = open(fileName, "r")
	dataSet = f.readlines()
	f.close()
	return dataSet

def printColorStr(str, colorSet):
	if (colorSet == "BLACK"):
		print(Color.BLACK + str + Color.END)
	elif (colorSet == "RED"):
		print(Color.RED + str + Color.END)
	elif (colorSet == "GREEN"):
		print(Color.GREEN + str + Color.END)
	elif (colorSet == "YELLOW"):
		print(Color.YELLOW + str + Color.END)
	elif (colorSet == "BLUE"):
		print(Color.BLUE + str + Color.END)
	elif (colorSet == "PURPLE"):
		print(Color.PURPLE + str + Color.END)
	elif (colorSet == "CYAN"):
		print(Color.CYAN + str + Color.END)
	elif (colorSet == "WHITE"):
		print(Color.WHITE + str + Color.END)

def putLine(str):
	backQuoteNum = 0
	for c in str:
		if (c == '`'):
			backQuoteNum = backQuoteNum + 1
	if (backQuoteNum == 0):
		print(str, end="")
		return
	else:
		i = 0
		while (str[i] != "`"):
			i = i + 1
		print(str[:i], end="")
		j = i+1
		while (str[j] != "`"):
			j = j + 1
		print(Color.RED + str[i+1:j] + Color.END, end="")
		line = str[j+1:]
		putLine(line)

def myprint(str, num):
	if (num == 1):
		putLine(str)
	elif (num == 0):
		putLine(str)
		print()

def printTitle(line):
	title = line[2:]
	titleLenght = len(title)
	myprint("=" * (titleLenght + 1), 0)
	myprint(" " + title, 1)
	myprint("=" * (titleLenght + 1), 0)
	print()

def printHeading1(line):
	heading = line[3:]
	headingLength = len(heading)
	myprint("-" * (1 + headingLength), 0)
	myprint(" " + heading, 1)
	myprint("-" * (1 + headingLength), 0)
	print()

def printQuote(line):
	quote = line[2:]
	quoteLen = len(quote)
	terminal_size = shutil.get_terminal_size()
	terminalColSize = terminal_size.columns

	myprint(" ╷", 0)
	if (quoteLen < (terminalColSize - 3)):
		myprint(" | " + quote, 0)
	else:
		i = 0
		while i < quoteLen:
			myprint(" | " + quote[i:i+terminalColSize - 5], 0)
			i = i + terminalColSize - 5

def putCodeTop(line):
	title = line[3:]
	titleLen = len(title)
	terminal_size = shutil.get_terminal_size()
	terminalColSize = terminal_size.columns

	print("--- " + line[3:-1] + " " + "-" * (terminalColSize - 4 - titleLen))

def putCodeMiddle(line):
	print(line, end="")

def putCodeEnd(line):
	terminal_size = shutil.get_terminal_size()
	terminalColSize = terminal_size.columns

	print("-" * terminalColSize)
	print()

def printHeading2(line):
	heading = line[4:]
	headingLength = len(heading)

	print()
	myprint(" " + heading, 1)
	myprint("~" * (1 + headingLength), 0)
	print()

def printHeading3(line):
	heading = line[4:]
	headingLength = len(heading)

	print()
	myprint(" " + heading, 1)
	myprint("-" * (1 + headingLength), 0)
	print()

def mdhub(line):
	global isCodeBlock
	global isQuote
	if (line[0:2] == "# "):
		printTitle(line)
	elif (line[0:3] == "## "):
		printHeading1(line)
	elif (line[0:4] == "### "):
		printHeading2(line)
	elif (line[0:5] == "#### "):
		printHeading3(line)
	elif (line[0:2] == "> "):
		printQuote(line)
		isQuote = 1
	elif (line[0:3] == "```"):
		if (isCodeBlock == 0):
			putCodeTop(line)
			isCodeBlock = 1
		elif (isCodeBlock == 1):
			putCodeEnd(line)
			isCodeBlock = 0
	elif (isCodeBlock == 1):
		putCodeMiddle(line)
	elif (line != '\n'):
		myprint(" " + line, 1)

def printMarkDown(dataSet):
	for line in dataSet:
		mdhub(line)

if __name__ == '__main__':
	args = sys.argv
	if len(args) != 2:
		errorHub(1)
	if (checkArg(args) == False):
		errorHub(2)
	readmeFilePath = args[1]
	dataSet = getDataSet(readmeFilePath)
	printMarkDown(dataSet)
