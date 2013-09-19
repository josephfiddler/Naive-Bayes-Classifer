class NaiveBayesClassifer:
	
	def parseDataFile(self, dataFile):
		listofVariables = []
		listOfInstances = []
		file = open (dataFile, 'rU')
		fileLines = file.readlines()

		#remove whitespace from files
		for line in fileLines:
			line= line.rstrip()
			if line:
				if line[0] == '#':   #check for comment
					x = 2
				elif line[0] == '@':	 #check for attribute
					listofVariables = self.parseLine(line)
				else:				# handle data
					tempInstance = self.Instance()
					valueList = self.parseLine(line)
					if len(listofVariables) < 1:
						print "Bad Data File"
						break
					
					for attr, value in zip(listofVariables, valueList):
						tempInstance.values[attr] = (value).lower()
					listOfInstances.append(tempInstance)

					# listOfInstances.append(Instance())
				
					# valueList = parseLine(line)
					# for attr,value in zip(listofVariables, valueList):
					# 	print attr + ":" + value
					# 	listOfInstances[-1].values[attr] = value
		
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
	print "Hello world"
	nbc = NaiveBayesClassifer()
	nbc.parseDataFile("/Users/Joey/Desktop/IntroToAI/rbes/data.txt")
	