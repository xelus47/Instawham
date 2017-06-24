#!/usr/bin/python2

import sys, commands

def out(a):
	if not type(a) is str:
		if hasattr(a,'__str__'):
			a = str(a)
		else:
			a = repr(a)
	sys.stdout.write(a)
	if sys.stdout.isatty():
		sys.stdout.write("\n")

if __name__=="__main__":
	pass
	#print sys.argv[0] # name of the file
	#print commands.getoutput("pwd") # path whence the call is made
