#You are given the following information, but you may prefer to do some research for yourself
#1 Jan 1900 was a Monday
#Thirty days has September,April, June and November.
#All the rest have thirty-one,
#Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#This could be done by using python libraries that support date, but I decided there is no fun in that.

monthsYear=[31,28,31,30,31,30,31,31,30,31,30,31]
monthsLeapYear=[31,29,31,30,31,30,31,31,30,31,30,31]

year0=1900
startYear=1901
endYear=2000
#1 Jan 1900 was a Monday -> 7 Jan Sunday
day=6

count=0
for y in range(year0, endYear+1):
	#find out if year is a leap year
	isLeap=False
	if(y%4==0):
		isLeap=True	
	if(y%100==0 and y%400>0):
		isLeap=False	
	
	for m in range(12):
		#count Sundays here, from 1901
		if(y>=startYear):
			if(day==0):
				count+=1
		#update day
		nDays=0
		if(isLeap):
			nDays=monthsLeapYear[m]
		else:
			nDays=monthsYear[m]
		while(day<nDays):
			day+=7
		day=day%nDays
	
print(count)	
		