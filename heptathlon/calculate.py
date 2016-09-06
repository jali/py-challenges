#!/usr/bin/python
import csv
import sys
import re
import os

# define tuples and dictionaries
units = ('100m', '200m', 'javelin', 'long')
throwjumplist = ['high', 'long', 'short', 'javelin']
weightings = {'200m' : (4.99087, 42.5, 1.81),
			'800m' : (0.11193, 254, 1.88),
			'100m' : (9.23076, 26.7, 1.835),
			'high' : (1.84523, 75.0, 1.348),
			'long' : (0.188807, 21.0, 1.41),
			'shot' : (56.0211, 1.50, 1.05),
			'javelin' : (15.9803, 3.80, 1.04)}

def throwjump(weight, value):
	if (float(value) > weightings[weight][1]):
		return str(int(weightings[weight][0] * int(float(value) - weightings[weight][1]) ** weightings[weight][2]))
	else:
		return "0"

def running(weight, value):
	if (float(value) < weightings[weight][1]):
		return str(int(weightings[weight][0] * int(weightings[weight][1] - float(value)) ** weightings[weight][2]))
	else:
		return "0"

dayList = {}
resultList = {}
#read argument and check if file extension is csv
arg_name = sys.argv[1]
name = re.split('\.', arg_name)[0]
ext = re.split('\.', arg_name)[1]

if (ext != "csv"):
	print "This calculator accepts csv file only as an argument. Please try again"
	quit()

# open file to read
try:
	f = open(arg_name, 'rb')
	with f:
		read = csv.reader(f)
		readList = list(read)

		d = 1
		# clean data
		for k, value in enumerate(readList):
			readList[k][0] = value[0].strip().lower()
			# set the initial results for all contestants
			resultList[value[0].strip().lower()] = 0

			readList[k][1] = value[1].strip().lower()
			if (value[1].strip().lower() in units):
				# clean record in row
				readList[k][2] = (re.findall("\d+\.\d+", value[2].strip()))[0]
				
			else:
				# search for minutes and update record in seconds
				minutes = (re.findall("\d+\:", value[2].strip()))[0][:-1]
				seconds = (re.findall(":\d+\.\d+", value[2].strip()))[0][1:]
				if (minutes):
					readList[k][2] = float(minutes * 60) + float(seconds)
				else:
					readList[k][2] = value[2].strip()

			readList[k][3] = re.findall("\d+\-\d+\-\d+", value[3].strip())[0]
			if (readList[k][3] != readList[k-1][3] or k==0):
				dayList[d] = readList[k][3]
				d += 1
	
	# calculation and output
	for day, date in dayList.iteritems():
		print "\n"
		print "---------------------------"
		print " Day " + str(day) + " " + date
		print "---------------------------"
		for v in readList:
			if (v[3] == date):
				# set initial value for points
				if(v[1] in throwjumplist):
					test = throwjump(v[1], v[2])
					resultList[v[0]] += int(test)
					print v[0].upper() + "\t\t" + str(resultList[v[0]])
				else:
					test2 = running(v[1], v[2])
					resultList[v[0]] += int(test2)
					print v[0].upper() + "\t\t" + str(resultList[v[0]])


# close the file
finally:
	f.close()
	dayList.clear()
	resultList.clear()

