from collections import defaultdict

class NaiveBayesClassifer:
	
	#Train Method
	def Train(self, dataFile):
		#Variable to hold the list of dictionaries returned from parseDataFile
		listOfDicts = self.parseDataFile(dataFile)
		
		#For each dictionary, variable list, and value list in the lists of listOfDicts, listOfVariables, and valueList
		for dict, attr, value in zip(listOfDicts, self.listOfVariables, self.valueList):
			#If the instance is a geek
			if (dict.Classification == "geek"):
				#For each variable and value in the lists attr and value
				for attr2, value2 in zip(attr, value):
					#If geekProbs doesn't have the key attr2
					if not self.geekProbs.has_key(attr2):
						#Then create a dictionary value for that key
						self.geekProbs[attr2] = {}
					if not self.geekProbs[attr2].has_key(value2):
						self.geekProbs[attr2][value2] = 1
					else:
						self.geekProbs[attr2][value2] += 1
			elif (dict.Classification == "non-geek"):
				for attr2, value2 in zip(attr, value):
					if not self.nongeekProbs.has_key(attr2):
						self.nongeekProbs[attr2] = {}
					if not self.nongeekProbs[attr2].has_key(value2):
						self.nongeekProbs[attr2][value2] = 1
					else:
						self.nongeekProbs[attr2][value2] += 1
				
		del self.geekProbs['class']
		del self.nongeekProbs['class']
		print self.geekProbs
		print self.nongeekProbs
					
				
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

		#remove whitespace from files
		for line in fileLines:
			line = line.rstrip()
			if line:
				if line[0] == '#':   #check for comment
					x = 2
				elif line[0] == '@':	 #check for attribute
					variables = self.parseLine(line)
					#print listofVariables #This prints all the @ variables that were in the data file
				else:				# handle data
					tempInstance = self.Instance()
					values = self.parseLine(line)
					
					#print valueList #This prints all the values for those variables
					if len(variables) < 1:
						print "Bad Data File"
						break
						
					for value in values:
						if (value == "geek"):
							geekCount = geekCount + 1
						elif (value == "non-geek"):
							nongeekCount = nongeekCount + 1
						
					
					self.geekProbs['prob'] = str(geekCount) + "/" + str(geekCount + nongeekCount)
					self.nongeekProbs['prob'] = str(nongeekCount) + "/" + str(geekCount + nongeekCount)
					
					#From what I can tell, this where the values are being put into the dictionaries.
					#This function and the Instace class is where we may need a dictionary of dictionaries
					#like on the Google doc. At least I narrowed down where the problem is. I believe once 					#we get the dictionary thing down, the rest of this program will be easy.
					for attr, value in zip(variables, values):
						tempInstance.values[attr] = (value).lower()
					listOfInstances.append(tempInstance)
					self.listOfVariables.append(variables)
					self.valueList.append(values)
		
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
			
	geekProbs = {}
	nongeekProbs = {}
	listOfVariables = []
	valueList = []
		
if __name__ == '__main__':
	nbc = NaiveBayesClassifer()
	nbc.Train("/Users/Joey/Desktop/IntroToAI/rbes/data.txt")
	