#!usr/bin/python

import webbrowser


url = "https://www.google.com/"

query = raw_input("\nWhat to search : ")
webbrowser.open_new(url+'/#q='+query)

print "\n Results fetched..!! \n"

execfile('loader.py')