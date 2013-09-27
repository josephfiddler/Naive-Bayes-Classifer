import math

class NaiveBayesClassifer:
	
	#Train method sets up the internal workings for the NBC
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
					#If geekProbs[attr2] doesn't have the key value2
					if not self.geekProbs[attr2].has_key(value2):
						#Then add 1 to the key
						self.geekProbs[attr2][value2] = 2.0
					#If geekProbs[attr2] has the key value2
					else:
						#Then increment
						self.geekProbs[attr2][value2] += 1.0
				#Keep a running count of geeks
				self.geekCount += 1.0
			#If the instance is a non-geek
			elif (dict.Classification == "non-geek"):
				#For each variable and value in the lists attr and value
				for attr2, value2 in zip(attr, value):
					#If nongeekProbs doesn't have the key attr2
					if not self.nongeekProbs.has_key(attr2):
						#Then create a dictionary value for that key
						self.nongeekProbs[attr2] = {}
					#If nongeekProbs[attr2] doesn't have the key value2
					if not self.nongeekProbs[attr2].has_key(value2):
						#Then add 1 to the key
						self.nongeekProbs[attr2][value2] = 2.0
					#If nongeekProbs[attr2] has the key value2
					else:
						#Then increment
						self.nongeekProbs[attr2][value2] += 1.0
				#Keep a running count of non-geeks
				self.nongeekCount += 1.0
				
		#Compute the total count of geeks and non-geeks
		self.totalCount = self.nongeekCount + self.geekCount
		
		#Create a key:value pair called prob for each dictionary
		self.geekProbs['prob'] = str(str(self.geekCount) + "/" + str(self.totalCount))
		self.nongeekProbs['prob'] = str(str(self.nongeekCount) + "/" + str(self.totalCount))
		
		#Delete the key class from both dictionaries. We don't need that.
		del self.geekProbs['class']
		del self.nongeekProbs['class']
		
	#Test method to classify some test data
	def Test(self, dataFile):
		#Variable to hold the list of dictionaries returned from parseDataFile
		listOfDicts = self.parseDataFile(dataFile)
		
		#Keep count of the corrent amount and total count
		correctCount = 0.0
		totalCount = 0.0
		
		#For each dictionary in the list of dictionaries
		for dict in listOfDicts:
			#If the classification matches the classification given to the dictionary from the Classify method
			if (dict.Classification == self.Classify(dict)):
				#Then it was correct, increment counts
				correctCount += 1.0
				totalCount += 1.0
			else:
				#If not, just increment the total count
				totalCount += 1.0
		
		#Return the percentage correct
		return correctCount / totalCount
			
	#Method to classify a instance
	def Classify(self, dict):
		#Variable to hold the starting probabilities
		geekProbability = self.geekCount / self.totalCount
		nongeekProbability = self.nongeekCount / self.totalCount
		
		#For each variable list and value list in the list of variables and value list
		for attr, value in zip(self.listOfVariables, self.valueList):
			#For each variable and value in the variable list and value list
			for attr2, value2 in zip(attr, value):
				#If geekProbs has the attr2 key
				if self.geekProbs.has_key(attr2):
					#If geekProbs has the key value2 in the attr2 dictionary
					if self.geekProbs[attr2].has_key(value2):
						#If key exists in geekProbs
						if (self.geekProbs[attr2].has_key(dict.values[attr2])):
							#Compute geekProbability
							geekProbability = geekProbability * math.log((self.geekProbs[attr2][dict.values[attr2]] / self.geekCount))
						elif (self.nongeekProbs[attr2].has_key(dict.values[attr2])):
							#Else, compute nongeekProbability
							nongeekProbability = nongeekProbability * math.log((self.nongeekProbs[attr2][dict.values[attr2]] / self.nongeekCount))
		
		#If geekProbability is greater than nongeekProbability
		if (geekProbability > nongeekProbability):
			#Then return geek
			return "geek"
		else:
			#Else return non-geej
			return "non-geek"
		
	def parseDataFile(self, dataFile):
		listofVariables = []
		listOfInstances = []
		file = open (dataFile, 'rU')
		fileLines = file.readlines()

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
					
					#From what I can tell, this where the values are being put into the dictionaries.
					#This function and the Instace class is where we may need a dictionary of dictionaries
					#like on the Google doc. At least I narrowed down where the problem is. I believe once 					#we get the dictionary thing down, the rest of this program will be easy.
					for attr, value in zip(variables, values):
						tempInstance.values[attr] = value
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
	geekCount = 1.0
	nongeekCount = 1.0
	totalCount = 2.0
	listOfVariables = []
	valueList = []
		
if __name__ == '__main__':
	nbc = NaiveBayesClassifer()
	nbc.Train("/Users/Joey/Desktop/IntroToAI/rbes/data.txt")
	print "The percentage correct is: ", nbc.Test("/Users/Joey/Desktop/IntroToAI/data2.txt")
	