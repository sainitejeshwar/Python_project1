#!usr/bin/python

from googlesearch import search

query=raw_input("Enter Query to search over https://www.google.com/ : ")
print 
search_result = search(query, tld="co.in", num=5, stop=1, pause=2)
print "Retriving Data ..... "
"""
	ARGUMENTS OF search()

	query : query string that we want to search for
	tld   : tld stands for top level domain
	num   : Number of results we want
	stop  : Last result to retrieve
	pause : Lapse to wait between HTTP requests
"""  
print
print "TOP 5 URL's :  " 
count=1
for i in search_result:
	if(count>5):
		break
	print count , " : " ,i 
	count  = count + 1
print
execfile('loader.py')