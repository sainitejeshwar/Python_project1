#!/usr/bin/python
from time import sleep

timer = 5

print "Returning back"
while(timer):
	print ".",
	timer=timer-1
	print " "
	sleep(0.5) 

execfile('main_menu.py')