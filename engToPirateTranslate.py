import re


with open('engToPirate.csv') as ep:


	wordDict = {}

	for line in ep:
		print(line)
		englishKey = line.rstrip().split(',')[0]
		pirateValue = line.rstrip().split(',')[1]

		wordDict[englishKey] = pirateValue

	del wordDict['English'] # this removes the headline from the dictionary. 
	print(wordDict)


	englishSentence = 'hello, my professor does not like your restaurant. But he likes to go to the restroom. hotel california and lawyer. list. "hello?". English'  
	print('begin: ',englishSentence)


	'''
	Option1:
	there would be a flaw using this method. For example, the word list will be replaced by 'is'->'be' and becomes 'lbet'
	'''
	# translating = False
	# for (k,v) in wordDict.items():

	# 	if translating == False:
	# 		pirateSentence = englishSentence.replace(k, v) # replace(key,value)
	# 		translating = True
	# 		print(pirateSentence)
	# 	else:
	# 		if k in 
	# 		pirateSentence = pirateSentence.replace(k,v)
	# 		print(pirateSentence)
	
	'''
	Option2:
	this method uses a boolean called translating to make sure that englishSentence don't get mutated. 
	but actually we don't have to do this. when we make a copy like this: pirateSentence = englishSentence
	we will keep the original englishSentence as it is. It doesn't get mutated. It doesn't reference to the same string.
	'''
	# translating = False	
	# for (k,v) in wordDict.items():
		
	# 	if translating == False:
	# 		# pirateSentence = re.sub(r'\b%s\b' % re.escape(k) ,v, englishSentence)
	# 		pirateSentence = re.sub(r'\b%s\b' % k ,v, englishSentence)
	# 		translating = True
	# 		print(pirateSentence)
	# 	else:	
	# 		pirateSentence = re.sub(r'\b%s\b' % k ,v, pirateSentence)
	# 		print(pirateSentence)
	# print(englishSentence)		
	# print('final version ', pirateSentence)

	'''
	Option3
	Here the regular regression is being used:  re.sub(pattern, new value, string to be replaced)
	re.sub is regular expression substitution 
	@'pattern' argument: is the way we want to replace the string (either partial or entire word)
	@'new value' argument: is what we want to replace as new values. 
	@string to be replaced: is the input for the sentence. 

	[NOTE] 
	r'\b%s\b' % variable <- gives us the privilage to change words as what we want variable to be. 
	Also now we don't have the issue of replacing partial string by mistake. 
	\b <- boundry
	r'' <- regular expression
	%s and % <- place holder (佔位符) 
	For example: k on dictionary(k,v) is old string, v is new string
	then we will have it become:
		re.sub(r'\b%s\b' % k ,v, sentence)
	'''
	pirateSentence = englishSentence
	for (k,v) in wordDict.items():
		
			pirateSentence = re.sub(r'\b%s\b' % k ,v, pirateSentence)
			print(r'\b%s\b' % k)
			print(pirateSentence)

	print(englishSentence)		
	print('final version: ', pirateSentence)



