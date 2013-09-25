from collections import defaultdict

class NaiveBayesClassifer:
				
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
					
					for attr in listofVariables:
						geekInstance.values.setdefault(attr, {})
					
					#Defnitely will have to use a Switch statement. Can't think of any other way, it will be huge
					#This is all test at the moment
					for attr, value in zip(listofVariables, valueList):
						if (value == "geek"):
							for attr2, value2 in zip(listofVariables, valueList):
								if (attr2 == "@gpa"):
									if (float(value2) > 3.6):
										geekDict[value2] += 1
										#geekInstance.values.setdefault(attr2, {})['gpa_3_6_orMore'] = 1
									else:
									    geekDict[value2] += 1
								
						elif (value == "non-geek"):
							for attr2, value2 in zip(listofVariables, valueList):
								if (attr2 == "@gpa"):
									if (float(value2) < 3.6):
										nongeekDict[value2] += 1
									else:
										nongeekDict[value2] += 1
								elif (attr2 == "@gender"):
									if (value2 == "Male"):
										nongeekDict[value2] += 1
									else:
										nongeekDict[value2] += 1
							
					
					
					'''		
					for attr, value in zip(listofVariables, valueList):
						if (attr == "@gender"):
							geekInstance.values.setdefault
						elif (attr == "@education"):
								
						elif (attr == "@relationship_status"):
							
						elif (attr == "@gpa"):
							
						elif (attr == "@major"):
							
						elif (attr == "@age"):
							
						elif (attr == "@employment"):
							
						elif (attr == "@ACT"):
							
						elif (attr == "@eyesight"):
							
						elif (attr == "@subject"):
							
						elif (attr == "@sports_cards"):
							
						elif (attr == "@magic"):
							
						elif (attr == "@comic_books"):
							
						elif (attr == "@action_figures"):
							
						elif (attr == "@transformers"):
							
						elif (attr == "@board_games"):
							
						elif (attr == "@video_games"):
							
						elif (attr == "@computer_games"):
							
						elif (attr == "@d&d"):
							
						elif (attr == "@sports"):
							
						elif (attr == "@bacon"):
							
						elif (attr == "@zombies"):
							
						elif (attr == "@pokemon"):
							
						elif (attr == "@anime"):
							
						elif (attr == "@game_system"):
							
						elif (attr == "@legos"):
							
						elif (attr == "@remote"):
							
						elif (attr == "@camping"):
							
						elif (attr == "@desktop_OS"):
							
						elif (attr == "@mobile_OS"):
							
						elif (attr == "@browser"):
							
						elif (attr == "@stackoverflow"):
							
						elif (attr == "@lifehacker"):
							
						elif (attr == "@slashdot"):
							
						elif (attr == "@hacker_news"):
							
						elif (attr == "@quora"):
							
						elif (attr == "@xkcd"):
							
						elif (attr == "@ccpp"):
							
						elif (attr == "@java"):
							
						elif (attr == "@obj_c"):
							
						elif (attr == "@php"):
							
						elif (attr == "@c_sharp"):
							
						elif (attr == "@python"):
							
						elif (attr == "@perl"):
							
						elif (attr == "@javascript"):
							
						elif (attr == "@lisp"):
							
						elif (attr == "@vb_net"):
							
						elif (attr == "@bash"):
							
						elif (attr == "@ruby"):
							
						elif (attr == "@star_wars_4_6"):
							
						elif (attr == "@star_wars_1_3"):
							
						elif (attr == "@lotr"):
							
						elif (attr == "@matrix"):
							
						elif (attr == "@tron1982"):
							
						elif (attr == "@tron2010"):
							
						elif (attr == "@spaceballs"):
							
						elif (attr == "@blade_runner"):
							
						elif (attr == "@xfiles"):
							
						elif (attr == "@fringe"):
							
						elif (attr == "@it_crowd"):
							
						elif (attr == "@mythbusters"):
							
						elif (attr == "@numb3rs"):
							
						elif (attr == "@dr_who_2005"):
							
						elif (attr == "@dr_who_1963"):
							
						elif (attr == "@battlestar_galactica_2004"):
							
						elif (attr == "@battlestar_galactica_1978"):
							
						elif (attr == "@star_trek"):
							
						elif (attr == "@wars_trek"):
							
						elif (attr == "@lotr_ee"):
							
						elif (attr == "@lotr_novels"): '''
							

					# listOfInstances.append(Instance())
				
					# valueList = parseLine(line)
					# for attr,value in zip(listofVariables, valueList):
					# 	print attr + ":" + value
					# 	listOfInstances[-1].values[attr] = value
		
		
		print geekDict.items()
		nongeekInstance.values.update(nongeekDict)
		
		print nongeekInstance.values
		#print nongeekInstance.values
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
	