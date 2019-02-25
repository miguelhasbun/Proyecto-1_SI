import sys
import random

def do_work():
	args = sys.argv
	args = args[1:] 
	if len(args) == 0:
		print('You have not written any commands!')
	else:
		for a in args:
			if a == 'grep':
				print('grep is a command-line utility for searching plain-text data sets for lines that match a regular expression')
			elif a == 'ping':
				print('The ping is used to test the ability of the source computer to reach a specified destination computer. ')
			elif a == 'ls':
				print('ls is a command to list computer files in Unix and Unix-like operating systems.')
			else:
				print('Unrecognised argument.')

if __name__ == '__main__':
	do_work()