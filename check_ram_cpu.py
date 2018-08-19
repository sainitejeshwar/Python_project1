#!/usr/bin/python
from os import popen
from psutil import virtual_memory,cpu_count , cpu_stats

ram = popen("free -m").readlines()[1].split()[1]
print "RAM 	 : ",ram , " MB"

print
vm_array=virtual_memory()
print "VIRTUAL MEMORY : "
print "		- Total      : " ,vm_array[0] ,"  Bytes"
print "		- Available  : ",vm_array[1],"  Bytes"
print "		- Used       : " ,vm_array[3],"  Bytes"
print "		- Percentage : ",vm_array[2],"  	     Bytes"

print
print "CPU CORES 	: " , cpu_count()

print 
cpu_stat_array = cpu_stats()
print "CPU STATS 	: "	
print "		- Interrupts  : " ,cpu_stat_array[1]
print "		- System Calls: " ,cpu_stat_array[-1]

execfile('loader.py')
