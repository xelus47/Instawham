#!/usr/bin/python2

import sys,os,argparse,json,time,urllib
import connect as wham_connect
sys.dont_write_bytecode = True


def fetch(path="/"):
	resp = wham_connect.get_response(path=path,host='www.instagram.com')
	assert resp.status==200, "%s %s @ %s%s"%(resp.status,resp.reason,'www.instagram.com',path)
	content_type = resp.getheader("content-type")
	if not content_type=="application/json":
		return resp.read()
	else:
		data = json.loads(resp.read())
		return data

def graphql(obj,query_id=None):
	""" access to /graphq/query/ """
	assert type(obj) is dict, "fetch.graphql: obj must be a dict"
	if query_id is None:
		f=open("query_id",'r')
		query_id=f.read()
		f.close()
	args = urllib.urlencode(obj)
	#data = fetch("/graphql/query/?"+args)
	return args

def main(url=None):
	if not sys.stdin.isatty() and url is None:
		for line in sys.stdin.readlines():
			line = line.replace("\n", "")
			if line!="":
				main(line)
		return 0

	parser = argparse.ArgumentParser(description="application/json-ish front end to connect.py")
	parser.add_argument("path",type=str,nargs="?",default="/",
		help = "path")
	
	args = parser.parse_args()
	if not url is None:
		args.path = url

	data = fetch(args.path)
	if type(data) is dict:
		print json.dumps(data, indent=2, sort_keys=True)
	else:
		print data

if __name__=="__main__":
	main()
	#graphql('60640649',first=12,after='1538433508471949457')
	#if not sys.stdin.isatty():
	#	main()
	#else:
	#	print graphql("60640649",first=12,after='1538433508471949457')
