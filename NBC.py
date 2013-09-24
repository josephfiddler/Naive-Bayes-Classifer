class NaiveBayesClassifer:
	
	def intializeDictionary(dictionary, variables):
		for attr in variables:
			if (attr == "@gender"):
				dictionary.values.setdefault['Male'] = 0
				dictionary.values.setdefault['Female'] = 0
			elif (attr == "@education"):
				dictionary.values.setdefault['High School or Equivalent'] = 0
				dictionary.values.setdefault['Bachelor\'s Degree'] = 0
				dictionary.values.setdefault['Master\'s Degree'] = 0
				dictionary.values.setdefault['Doctorate Degree'] = 0
			elif (attr == "@relationship_status"):
				dictionary.values.setdefault['Single'] = 0
				dictionary.values.setdefault['Married'] = 0
				dictionary.values.setdefault['In a relationship'] = 0
				dictionary.values.setdefault['It\'s complicated'] = 0
			elif (attr == "@gpa"):
				dictionary.values.setdefault['2.0-3.0'] = 0
				dictionary.values.setdefault['3.0-3.4'] = 0
				dictionary.values.setdefault['3.4-3.8'] = 0
				dictionary.values.setdefault['3.8-4.0'] = 0
			elif (attr == "@major"):
				dictionary.values.setdefault
			elif (attr == "@age"):
				dictionary.values.setdefault
			elif (attr == "@employment"):
				dictionary.values.setdefault
			elif (attr == "@ACT"):
				dictionary.values.setdefault
			elif (attr == "@eyesight"):
				dictionary.values.setdefault
			elif (attr == "@subject"):
				dictionary.values.setdefault
			elif (attr == "@sports_cards"):
				dictionary.values.setdefault
			elif (attr == "@magic"):
				dictionary.values.setdefault
			elif (attr == "@comic_books"):
				dictionary.values.setdefault
			elif (attr == "@action_figures"):
				dictionary.values.setdefault
			elif (attr == "@transformers"):
				dictionary.values.setdefault
			elif (attr == "@board_games"):
				dictionary.values.setdefault
			elif (attr == "@video_games"):
				dictionary.values.setdefault
			elif (attr == "@computer_games"):
				dictionary.values.setdefault
			elif (attr == "@d&d"):
				dictionary.values.setdefault
			elif (attr == "@sports"):
				dictionary.values.setdefault
			elif (attr == "@bacon"):
				dictionary.values.setdefault
			elif (attr == "@zombies"):
				dictionary.values.setdefault
			elif (attr == "@pokemon"):
				dictionary.values.setdefault
			elif (attr == "@anime"):
				dictionary.values.setdefault
			elif (attr == "@game_system"):
				dictionary.values.setdefault
			elif (attr == "@legos"):
				dictionary.values.setdefault
			elif (attr == "@remote"):
				dictionary.values.setdefault
			elif (attr == "@camping"):
				dictionary.values.setdefault
			elif (attr == "@desktop_OS"):
				dictionary.values.setdefault
			elif (attr == "@mobile_OS"):
				dictionary.values.setdefault
			elif (attr == "@browser"):
				dictionary.values.setdefault
			elif (attr == "@stackoverflow"):
				dictionary.values.setdefault
			elif (attr == "@lifehacker"):
				dictionary.values.setdefault
			elif (attr == "@slashdot"):
				dictionary.values.setdefault
			elif (attr == "@hacker_news"):
				dictionary.values.setdefault
			elif (attr == "@quora"):
				dictionary.values.setdefault
			elif (attr == "@xkcd"):
				dictionary.values.setdefault
			elif (attr == "@ccpp"):
				dictionary.values.setdefault
			elif (attr == "@java"):
				dictionary.values.setdefault
			elif (attr == "@obj_c"):
				dictionary.values.setdefault
			elif (attr == "@php"):
				dictionary.values.setdefault
			elif (attr == "@c_sharp"):
				dictionary.values.setdefault
			elif (attr == "@python"):
				dictionary.values.setdefault
			elif (attr == "@perl"):
				dictionary.values.setdefault
			elif (attr == "@javascript"):
				dictionary.values.setdefault
			elif (attr == "@lisp"):
				dictionary.values.setdefault
			elif (attr == "@vb_net"):
				dictionary.values.setdefault
			elif (attr == "@bash"):
				dictionary.values.setdefault
			elif (attr == "@ruby"):
				dictionary.values.setdefault
			elif (attr == "@star_wars_4_6"):
				dictionary.values.setdefault
			elif (attr == "@star_wars_1_3"):
				dictionary.values.setdefault
			elif (attr == "@lotr"):
				dictionary.values.setdefault
			elif (attr == "@matrix"):
				dictionary.values.setdefault
			elif (attr == "@tron1982"):
				dictionary.values.setdefault
			elif (attr == "@tron2010"):
				dictionary.values.setdefault
			elif (attr == "@spaceballs"):
				dictionary.values.setdefault
			elif (attr == "@blade_runner"):
				dictionary.values.setdefault
			elif (attr == "@xfiles"):
				dictionary.values.setdefault				elif (attr == "@fringe"):
				dictionary.values.setdefault
			elif (attr == "@it_crowd"):
				dictionary.values.setdefault
			elif (attr == "@mythbusters"):
				dictionary.values.setdefault	
			elif (attr == "@numb3rs"):
				dictionary.values.setdefault	
			elif (attr == "@dr_who_2005"):
				dictionary.values.setdefault	
			elif (attr == "@dr_who_1963"):
				dictionary.values.setdefault
			elif (attr == "@battlestar_galactica_2004"):
				dictionary.values.setdefault	
			elif (attr == "@battlestar_galactica_1978"):
				dictionary.values.setdefault	
			elif (attr == "@star_trek"):
				dictionary.values.setdefault	
			elif (attr == "@wars_trek"):
				dictionary.values.setdefault	
			elif (attr == "@lotr_ee"):
				dictionary.values.setdefault	
			elif (attr == "@lotr_novels"):
				dictionary.values.setdefault
				
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
					listofVariables = self.parseLine(line)
					#print listofVariables #This prints all the @ variables that were in the data file
				else:				# handle data
					tempInstance = self.Instance()
					valueList = self.parseLine(line)
					
					print valueList
					
					
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
										
										geekInstance.values.setdefault(attr2, {})['gpa_3_6_orMore'] += 1
									else:
										geekInstance.values.setdefault(attr2, {})['gpa_3_6_orLess'] += 1
						elif (value == "non-geek"):
							nongeekInstance.values.setdefault(attr, {})['gpa_3_6_orLess'] = value
					
					
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
		
		
		print geekInstance.values
		print nongeekInstance.values
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
	