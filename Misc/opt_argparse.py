# Author : AL
# Usage  : python3  opt_argparse.py -s source -d dest -c compose


#!/usr/bin/python3

import argparse
import sys, os


# define parser=argparse.ArgumentParser()
# then call this function add_arg(parser, '-s', '--source', help_msg='Source file name', require='True') for each option
def add_arg(parser, short_opt, long_opt, help_msg='Cannot be empty', require='False'):
	if require :
#		print (require)
		parser.add_argument(short_opt, long_opt, help=help_msg, required=require)
	else:
#		print("none require")
		parser.add_argument(short_opt, long_opt, help=help_msg)

def create_3options():
	print ("\n")
	parser=argparse.ArgumentParser(add_help=True)
	add_arg(parser, '-s', '--source', help_msg='Source file name', require='True')
	add_arg(parser, '-d', '--destination', help_msg='Destination file name', require='True')
	add_arg(parser, '-c', '--compose', help_msg='Compose file name')
	args = parser.parse_args()
	return args

def print_3options(args):
	## show values ##
	print ("Input file :  %s" % args.source  )
	print ("Output file:  %s" % args.destination )
	print ("Compose file: %s" % args.compose )
	print ("\n" )


def main():
	my3opts = []
	my3opts=create_3options()
	print_3options(my3opts)


if __name__ == "__main__":
	main()
