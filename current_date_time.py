
#!/usr/bin/python
from time import ctime
curr_date_time = ctime().split(' ')  # format : Sat Aug 18 HH:MM:SS 2018
curr_date = curr_date_time[2] + " " + curr_date_time[1] + " " + curr_date_time[-1]
curr_time = map(int,curr_date_time[-2].split(":"))
hour = curr_time[0]%12 if curr_time[0] > 12 else curr_time[0]
am_or_pm = "  a.m." if hour < 12 else "  p.m."
print "DATE : " , curr_date
print "TIME : " , hour , ":" ,curr_time[1] , ":",curr_time[2], am_or_pm
execfile('loader.py')
