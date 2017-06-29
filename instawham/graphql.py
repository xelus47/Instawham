#!/usr/bin/python2

import json, os, sys, urllib
sys.dont_write_bytecode = True

from fetch import fetch as arcesse # imperative (because it's a function I call imperatively)
import output



def grapql_resolve(**kwargs): # istaypuffed
	""" actual args: category,query[,first,after] """
	# TODO: optional config file?? ("grapql.json")
	query_ids={'user':17880160963012870,
		'location':17881432870018455,
		'hashtag':17882293912014529,
		'comments':17852405266163336,
	}
	q_params={'user':'id',
		'location':'id',
		'hashtag':'tag_name',
		'comments':'shortcode',
	}
	# TODO: continue coding...


def graphql(obj):
	""" -> dict """
	if not type(obj) is dict:
		raise NotImplementedError("Graphql parameter must be a <type \'dict\'>")
	required = ['query_id']
	any_of_these = ['id','tag_name','shortcode']
	optional = ['first','after']
	if not all(field in obj for field in required):
		raise KeyError("Supply at least all of %s"%repr(required))
	if not any(field in obj for field in any_of_these):
		raise KeyError("Supply at least one of %s"%repr(any_of_these))
	# after these checks, the input is asserted to be correct

	query_str = urllib.urlencode(obj)
	data = arcesse("/graphql/query/?"+query_str) 
	# arcesse returns json dict if header(content_type)==json
	if not type(data) is dict:
		output.e_out("Remote server: www.instagram.com/grapql/query/?"+query_str)
		raise AssertionError("Remote server did not return json content.")
	else:
		return data


if __name__=="__main__":
	sys.stdout.write("Hello, world\n")
	
