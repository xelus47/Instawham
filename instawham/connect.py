#!/usr/bin/python2

import sys,os,httplib,argparse,threading,time,re
import output # .py
sys.dont_write_bytecode = True

def connect(path="/",host="localhost",user_agent=None,method="GET"):
	# make HTTPS connection to specified host and path with method
	resp = get_response(path,host,user_agent,method)
	# throw assertion error if not OK
	assert resp.status==200, "%s %s @ %s%s"%(resp.status,resp.reason,host,path)
	# return body
	# if you need the headers too, use get_response in code or -t option in terminal
	return resp.read()

def closesock(sock,timeout=1):
	time.sleep(timeout)
	sock.close()

def get_response(path="/",host="localhost",user_agent=None,method='GET'):
	if user_agent is None:
		user_agent='Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/53.0' # firefox 53 in win7
	
	conn = httplib.HTTPSConnection(host)
	conn.putrequest(method,path)
	conn.putheader("user-agent",user_agent)
	conn.endheaders()

	# give main thread some time
	# to process the response
	# before closing socket
	#closing = threading.Thread(target=closesock,args=(conn,))
	#closing.run()

	return conn.getresponse()

	

def main(url=None):
	if not sys.stdin.isatty() and url is None:
		for line in sys.stdin.readlines():
			line = line.replace("\n","")
			main(line) # recursively run every line
		return 0 # and then exit
	
	parser=argparse.ArgumentParser(description="Simple HTTPLib front-end",conflict_handler='resolve')
	parser.add_argument("path",nargs="?",default="/",type=str,
		help = "GET [path]",metavar='path')
	parser.add_argument("host",nargs="?",default="www.instagram.com",type=str,
		help = "hostname",metavar='hostname')
	parser.add_argument("--host",dest="host2",nargs="?",default=None,type=str,
		help = "overrides the other hostname argument", metavar="hostname")
	parser.add_argument("-v",action="count",default=0,
		help = "verbosity")
	parser.add_argument("-t","--test",action='store_true',default=False,
		help = "only request HEAD")
	args = parser.parse_args()
	
	if not args.host2 is None:
		args.host = args.host2
	delattr(args,'host2')

	if not url is None:
		args.path = url
	if args.v>=3:
		print args

	if args.test:
		method = "HEAD"
	else:
		method = "GET"

	# finally, make connection
	if not args.v:
		try:
			data = connect(path=args.path,host=args.host,method=method)
			output.out(data)
			return 0
		except AssertionError as e:
			output.err_out(e)
			return 1
	else:
		resp = get_response(path = args.path, host = args.host, method=method)
		print "%s%s - %s %s"%(args.host,args.path,resp.status,resp.reason)
		if args.v>=2:
			for header in resp.getheaders():
				print "%s: %s"%header
		output.out(resp.read())
		return 0


if __name__=="__main__":
	main()
	

