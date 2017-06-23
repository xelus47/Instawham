#!/usr/bin/python2

import sys, commands

if __name__=="__main__":
	print sys.argv[0] # name of the file
	print commands.getoutput("pwd") # path whence the call is made
