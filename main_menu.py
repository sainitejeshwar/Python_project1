#!/usr/bin/python

options = """ 
  ~~~~~~~~~~~~~~~~~~~~~OPTIONS~~~~~~~~~~~~~~~~~~~~~~

1 : Current Date and Time
2 : Check RAM and CPU Status
3 : Open Deafult Web Browser of your current OS
4 : Open Camera
5 : Reboot your sysytem
6 : Search something on the Google
7 : Scan all MAC address of your current network
8 : Search on https://www.google.com/ and list top 5 URL'S list on search result
9 : Logout your current OS account 
0 : Exit"""

print options
print

choice = raw_input("Option : ")

#check for character input
try : 
	choice=int(choice)
except ValueError:
	choice = -1


if( choice == 1 ):
	execfile('current_date_time.py')
elif( choice == 2 ):
	execfile('check_ram_cpu.py')
elif( choice == 3 ):
	execfile('web_search.py')
elif( choice == 4 ):
	execfile('open_cam.py')
elif( choice == 5 ):
	execfile('reboot.py')
elif( choice == 6 ):
	execfile('google_search.py')
elif( choice == 7 ):
	execfile('mac_add.py')
elif( choice == 8 ):
	execfile('search_output.py')
elif( choice == 9 ):
	execfile('logout_user.py')
elif( choice == 0 ):
	print "Aborting ...."
else:
	print "Invalid Input ..!!"
	execfile('loader.py')

#main ends