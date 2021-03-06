import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	File = open(file, "r")
	s_infoLst = []
	headers = File.readline()
	lines = File.readlines()
	for line in lines:
		s_info = {}
		item = line.split(",")
		first = item[0]
		last = item[1]
		email = item[2]
		c_year = item[3]
		birthday = item[4]
		line = File.readline()
		s_info["First"] = first
		s_info["Last"] = last
		s_info["Email"] = email
		s_info["Class"] = c_year
		s_info["DOB"] = birthday
		s_infoLst.append(s_info)
	File.close()
	return s_infoLst

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sort_dict=sorted(data, key=lambda val: val[col])

	y = sort_dict[0]
	s_first = y['First']
	s_last = y['Last']

	return s_first + " " + s_last

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	lst_tuples = []
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	for x in data:
		if x['Class'] == 'Freshman':
			freshman+=1
		elif x['Class'] == 'Sophomore':
			sophomore+=1
		elif x['Class'] == 'Junior':
			junior+=1
		elif x['Class'] == 'Senior':
			senior+=1
	lst_tuples.append(('Freshman', freshman))
	lst_tuples.append(('Sophomore', sophomore))
	lst_tuples.append(('Junior', junior))
	lst_tuples.append(('Senior', senior))

	sort_tuple=sorted(lst_tuples, key=lambda val: val[1], reverse = True)
	return sort_tuple

def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	lst_months = []
	common_month={}
	for x in a:
		y=x['DOB']
		lst=y.split('/')
		lst_months.append(lst[0])
	for x in lst_months:
		if x in common_month:
			common_month[x]+=1
		else:
			common_month[x]=1

	sort_months=sorted(common_month, key=common_month.get, reverse = True)
	return int(sort_months[0])


def mySortPrint(a,col,fileName):
# Similar to mySort, but instead of returning single
# Student, the sorted data is saved to a csv file.
# as fist,last,email
# Input: list of dictionaries, col (key) to sort by and output file name
# Output: No return value, but the file is written
	s_csv = open(fileName, 'a')

	sort_dict = sorted(a, key=lambda val: val[col])

	for s in sort_dict:
		s_first = s['First']
		s_last = s['Last']
		s_email = s['Email']
		string = s_first + "," + s_last + "," + s_email + "\n"
		s_csv.write(string)

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	c_ages=[]
	for s_info in a:
		birthday = s_info['DOB']. split('/')
		year = birthday[2]
		age = 2018 - int(year)
		c_ages.append(age)
	avg_age = sum(c_ages) / len(c_ages)
	return round(avg_age)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
