#!/usr/bin/python2

import sys,os,httplib,argparse,threading,time

def connect(path="/",host="/",user_agent=None):
	resp = get_response(path,host,user_agent)
	assert resp.status==200, "%s %s @ %s%s"%(resp.status,resp.reason,host,path)
	return resp.read()

def closesock(sock,timeout=1):
	time.sleep(timeout)
	sock.close()

def get_response(path="/",host="/",user_agent=None):
	if user_agent is None:
		user_agent='Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/47.0' # firefox 47 in win7
	
	conn = httplib.HTTPSConnection(host)
	conn.putrequest("GET",path)
	conn.putheader("user-agent",user_agent)
	conn.endheaders()

	# give main thread some time
	# to process the response
	# before closing socket
	closing = threading.Thread(target=closesock,args=(conn,))
	closing.run()

	return conn.getresponse()


