import csv
import sys
#First figuring out using a given filename and given date
#For Running the File, run it as python3 ./most_active_cookie.py cookie_log.csv -d <Date that you want to use>

def cookie_function(date_name, file_name):
	date = date_name
	filename = file_name
	counter = 0
	list_of_lists = [];
	with open(filename, "r") as datfile:
		sheetreader = csv.reader(datfile, delimiter = ",")
		for line in sheetreader:
			list_of_lists.append([])
			list_of_lists[counter].append(line[0])
			list_of_lists[counter].append(line[1])
			counter+=1
			

	cookie_dict = {}
	for item in list_of_lists:
		key = item[0]
		dateAndTime = item[1].split("T")
		if dateAndTime[0] == date:
			if key in cookie_dict.keys():
				cookie_dict[key] = cookie_dict[key]+1
			else:
				cookie_dict[key] = 1
	
	if len(cookie_dict) == 0:
		return
	
	maxValue = max(cookie_dict.values())

	for item in cookie_dict.keys():
		if cookie_dict[item] == maxValue:
			print(item)
		else:
			continue

#arg test
#print(str(sys.argv))
#Tests
print("Test 1: 2018-12-09")
date_name = "2018-12-09"
file_name = "./cookie_log.csv"
print("Date:", date_name)
print("Filename:", file_name)
print()
print("Answer")
cookie_function(date_name, file_name)
print()

print("Test 2: 2018-12-08")
date_name = "2018-12-08"
file_name = "./cookie_log.csv"
print("Date:", date_name)
print("Filename:", file_name)
print()
print("Answer")
cookie_function(date_name, file_name)
print()

print("Test 3: Using Arguments")
date_name = str(sys.argv[3])
file_name = str(sys.argv[1])
print("Date:", date_name)
print("Filename:", file_name)
print()
print("Answer")
cookie_function(date_name, file_name)
print()




#for val in list_of_lists:
#	print(val[0])
#	print(val[1])
#	print()

