# Author : AL
# Usage  : python3  opt_argparse.py -i inputfile -o outputfile


#!/usr/bin/python3

import argparse
import sys, os


def add_arg(parser, short_opt, long_opt, help_msg='Cannot be empty', require=True):
	parser.add_argument(short_opt, long_opt, help=help_msg, required=require)


print ("\n")
parser=argparse.ArgumentParser()
add_arg(parser, '-s', '--source', help_msg='Source file name', require='True')
add_arg(parser, '-d', '--destination', help_msg='Destination file name', require='True')
add_arg(parser, '-c', '--compose', help_msg='Compose file name', require='False')
args = parser.parse_args()


## show values ##
print ("Input file : %s" % args.input  )
print ("Output file: %s" % args.output )
print ("Compose file: %s" % args.compose )
print ("\n" )
