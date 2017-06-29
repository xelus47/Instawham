#!/usr/bin/python2

import sys,os,argparse,json,time,urllib
import connect as wham_connect
sys.dont_write_bytecode = True


def fetch(path="/"):
	""" -> str or dict """
	resp = wham_connect.get_response(path=path,host='www.instagram.com')
	assert resp.status==200, "%s %s @ %s%s"%(resp.status,resp.reason,'www.instagram.com',path)
	content_type = resp.getheader("content-type")
	if not content_type=="application/json":
		return resp.read()
	else:
		data = json.loads(resp.read())
		return data

def graphql_success(s):
	""" s -> bool """
	""" returns True if it is parsed by json and is of acceptable format """
	""" acceptable format: { "data" : { "category" (...) """
	""" caveat: two types of queries use 'id', namely LOCATION and USER,
	    so choosing the incorrect query_id does not raise an error, but
	    yields exactly zero results """
	
	try:
		query = json.loads(s)
	except ValueError:
		return False
	
	if not 'data' in query:
		return False
	else:
		if 'location' in query['data']:
			pass
		return True


def graphql(obj,query_ids=None):
	""" access to /graphq/query/ """
	if not type(obj) is dict:
		raise TypeError("Expecting dict type variable")
	if type(query_ids) is list:
		query_ids="\n".join(query_ids)
	if query_ids is None:
		f=open("query_id",'r')
		query_ids=f.read()
		f.close()
	
	
	args = urllib.urlencode(obj)
	#data = fetch("/graphql/query/?"+args)
	return args

def main(url=None):
	""" -> none """
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
