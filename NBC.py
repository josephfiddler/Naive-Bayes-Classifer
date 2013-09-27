from collections import defaultdict

class NaiveBayesClassifer:
	
	def Test(self, dataFile):
		listOfDicts = 
				
	def parseDataFile(self, dataFile):
		listofVariables = []
		listOfInstances = []
		file = open (dataFile, 'rU')
		fileLines = file.readlines()
		
		#Declare variables to keep count of the geeks and those heathen non-geeks
		geekCount = 0
		nongeekCount = 0
		count = 0
		
		#Create geek and non-geek dictionaries
		geekInstance = self.Instance()
		nongeekInstance = self.Instance()
		geekDict = defaultdict(int)
		nongeekDict = defaultdict(int)
		nonGeekProbs = defaultdict(dict)

		#remove whitespace from files
		for line in fileLines:
			line = line.rstrip()
			if line:
				if line[0] == '#':   #check for comment
					x = 2
				elif line[0] == '@':	 #check for attribute
					listofVariables = self.parseLine(line)
					#print listofVariables #This prints all the @ variables that were in the data file
				else:				# handle data
					tempInstance = self.Instance()
					valueList = self.parseLine(line)
					
					#print valueList #This prints all the values for those variables
					if len(listofVariables) < 1:
						print "Bad Data File"
						break
						
					for value in valueList:
						if (value == "geek"):
							geekCount = geekCount + 1
						elif (value == "non-geek"):
							nongeekCount = nongeekCount + 1
						
					
					geekInstance.values['prob'] = str(geekCount) + "/" + str(geekCount + nongeekCount)
					nongeekInstance.values['prob'] = str(nongeekCount) + "/" + str(geekCount + nongeekCount)
					
					#From what I can tell, this where the values are being put into the dictionaries.
					#This function and the Instace class is where we may need a dictionary of dictionaries
					#like on the Google doc. At least I narrowed down where the problem is. I believe once 					#we get the dictionary thing down, the rest of this program will be easy.
					for attr, value in zip(listofVariables, valueList):
						tempInstance.values[attr] = (value).lower()
					listOfInstances.append(tempInstance)
					
					#Defnitely will have to use a Switch statement. Can't think of any other way, it will be huge
					#This is all test at the moment
					if (tempInstance.Classification == "geek"):
						for attr2, value2 in zip(listofVariables, valueList):
							if not geekInstance.values.has_key(attr2):
								geekInstance.values[attr2] = {}
							if not geekInstance.values[attr2].has_key(value2):
								geekInstance.values[attr2][value2] = 1
							else:
								geekInstance.values[attr2][value2] += 1
					elif (tempInstance.Classification == "non-geek"):
						for attr2, value2 in zip(listofVariables, valueList):
							if not nongeekInstance.values.has_key(attr2):
								nongeekInstance.values[attr2] = {}
							if not nongeekInstance.values[attr2].has_key(value2):
								nongeekInstance.values[attr2][value2] = 1
							else:
								nongeekInstance.values[attr2][value2] += 1
							
					nongeekDict.clear()
		
		
		print nongeekInstance.values
		print geekInstance.values
		
		return listOfInstances
		
	def parseLine(self, line): #parses variables on an @ line
		wordList = line.split("\t") #put each word into list 
		return wordList
		
	class Instance:
		values = {} #dictionary entries
		@property  #the actual classification of the Instance
		def Classification(self):
			return self.values['class']
		def __init__(self):
			self.values = {}
		def __repr__(self):
			return str(self.values) + " ("+ self.Classification + ")"
		
if __name__ == '__main__':
	nbc = NaiveBayesClassifer()
	nbc.parseDataFile("/Users/Joey/Desktop/IntroToAI/rbes/data.txt")
	