#!/usr/bin/python2

import sys, commands

def __format(a):
	if not type(a) is str:
		if hasattr(a,'__str__'):
			a = str(a)
		else:
			a = repr(a)
	return a

def err_out(a):
	a = __format(a)
	sys.stderr.write(a)
	if sys.stderr.isatty():
		sys.stdout.write("\n")

def out(a):
	a = __format(a)
	sys.stdout.write(a)
	if sys.stdout.isatty():
		sys.stdout.write("\n")

if __name__=="__main__":
	out("Standard output")
	err_out("Standard error")
	#print sys.argv[0] # name of the file
	#print commands.getoutput("pwd") # path whence the call is made
