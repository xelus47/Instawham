#!/usr/bin/python2

import httplib, os, sys, json, time

if __name__=="__main__":
	#print "stdin:",sys.stdin.isatty()
	#print "stdout:",sys.stdout.isatty()
	#print "stderr:",sys.stderr.isatty()
	if not sys.stdin.isatty():
		sys.stdout.write("stdin lines "+str(len(sys.stdin.read().split("\n")))+"\n")
	sys.stdout.write("stdout\n")
	sys.stderr.write("stderr\n")
	sys.exit()
