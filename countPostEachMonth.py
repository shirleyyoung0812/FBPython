#this script is used to count number of posts and likes of a company
import iso8601
from iso8601 import ParseError
import os
import datetime

def isTimeFormat(line): 
	try: 
		iso8601.parse_date(line)
		return True
	except ParseError:
		return False

def isPost(line):
	if line:
		if line.strip():
			if not isTimeFormat(line):
				return True
	else:
		return False


def main():
	path = "/Users/shirleyyoung/Documents/pythonfile/FBposts/companyData"
	companyLists = os.listdir(path)
	output = open('c.csv', 'w')
	output.write("FB account,year,month,number of posts\n")
	os.chdir(path)
	for companyName in companyLists:
		with open(companyName, 'r') as company:
			comp = companyName.replace(",", " ")[:-4]
			print(comp)
			count = 0
			lastLine = False
			FirstLine = True
			firstDate = True
			curMonth = 0
			curYear = 0
			likes = 0
			startingDate = datetime.date.today()
			for line in company:
				if (FirstLine):
					tmp = line.split(" ")
					likes = int(tmp[len(tmp) - 2])
					FirstLine = False
				if(isTimeFormat(line)):
					date = iso8601.parse_date(line)
					if (firstDate):
						startingDate = date
						firstDate = False
					if (curMonth == 0):
						curYear = date.year
						curMonth = date.month
					if (curMonth != date.month):
						output.write("{},{},{},{}\n".format(comp, curYear, curMonth, count))
						count = 0
						curYear = date.year
						curMonth = date.month
					#print("{}, {}".format(date.year, date.month)) 
					lastLine = True
					#print(line)
				if (isPost(line)):
					if(lastLine):
						count += 1
						#print(line, count)
						#print("*******")
						lastLine = False
			output.write("{},{},{},{}\n".format(comp, curYear, curMonth, count))
			endingDate = date
			output.write("{},{},{}\n".format(comp, startingDate, endingDate))
			output.write("\n")
		company.close()
	output.close()

main()
