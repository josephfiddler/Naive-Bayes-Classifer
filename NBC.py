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
					
					for attr in listofVariables:
						geekInstance.values.setdefault(attr, {})
					
					#Defnitely will have to use a Switch statement. Can't think of any other way, it will be huge
					#This is all test at the moment
					for attr, value in zip(listofVariables, valueList):
						if (value == "geek"):
							for attr2, value2 in zip(listofVariables, valueList):
								geekDict[value2] += 1
								
								if not geekInstance.values.has_key(attr2):
									geekInstance.values[attr2] = {}
								if not geekInstance.values[attr2].has_key(value2):
									geekInstance.values[attr2][value2] = 1
								else:
									geekInstance.values[attr2][value2] += 1
								
						elif (value == "non-geek"):
							for attr2, value2 in zip(listofVariables, valueList):
								nongeekDict[value2] += 1
								#nonGeekProbs[attr2].update(nongeekDict)
								if not nongeekInstance.values.has_key(attr2):
									nongeekInstance.values[attr2] = {}
								if not nongeekInstance.values[attr2].has_key(value2):
									nongeekInstance.values[attr2][value2] = 1
								else:
									nongeekInstance.values[attr2][value2] += 1
								#nongeekInstance.values[attr2][value2] = nongeekDict[value2]
									#if not nongeekInstance.values[attr2].has_key(value2):
										#nongeekInstance.values[attr2][value2] = {}
								#nongeekInstance.values[attr2][value2] = nongeekDict[value2]
								#nongeekInstance.values[attr2][value2] = nongeekDict[value2]
								
								'''if (attr2 == "@gpa"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
									break'''
								'''if (attr2 == "@gender"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@education"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
									break
								elif (attr2 == "@relationship_status"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@major"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@age"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@employment"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@ACT"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@eyesight"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@subject"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@sports_cards"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@magic"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@comic_books"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@action_figures"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@transformers"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@board_games"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@video_games"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@computer_games"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@d&d"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@sports"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@bacon"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@zombies"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@pokemon"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@anime"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@game_system"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@legos"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@remote"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@camping"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@desktop_OS"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@mobile_OS"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@browser"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@stackoverflow"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@lifehacker"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@slashdot"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@hacker_news"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@quora"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@xkcd"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@ccpp"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@java"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@obj_c"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@php"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@c_sharp"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@python"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@perl"):
									nongeekDict[value2] += 1
									#nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@javascript"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@lisp"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@vb_net"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@bash"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@ruby"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@star_wars_4_6"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@star_wars_1_3"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@lotr"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@matrix"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@tron1982"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@tron2010"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@spaceballs"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@blade_runner"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@xfiles"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@fringe"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@it_crowd"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@mythbusters"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@numb3rs"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@dr_who_2005"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@dr_who_1963"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@battlestar_galactica_2004"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@battlestar_galactica_1978"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@star_trek"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@wars_trek"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@lotr_ee"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)
								elif (attr2 == "@lotr_novels"):
									nongeekDict[value2] += 1
									nongeekInstance.values.setdefault(attr2, {}).update(nongeekDict)'''
									
								
						nongeekDict.clear()
						#nongeekInstance.values.setdefault('@gpa', {}).update(nongeekDict.fromkeys(nongeekDict.keys()))
						
							
					

					# listOfInstances.append(Instance())
				
					# valueList = parseLine(line)
					# for attr,value in zip(listofVariables, valueList):
					# 	print attr + ":" + value
					# 	listOfInstances[-1].values[attr] = value
		
		
		#print geekDict.items()
		#nongeekInstance.values.update(nongeekDict)
		#print nongeekDict.items()
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
	