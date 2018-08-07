

with open('Alices_Adventures.txt') as book:


	wordDict = {}
	sentenses = []


	# this for loop strips out '\n' from each end of the line, then split each word by ' '.
	# now we have a list of words like this: ["a", "b", "c"],["d","e"]... (each line)
	# next we add them to the sentenses list so that we don't have to deal with list of lists again. 
	# we use 'sentenses = sentenses + words' instead of 'sentenses.append(words)'
	# for example: 'sentenses = sentenses + words' -> ["a","b","c","d","e"]
	# and 'sentenses.append(words)' -> [["a","b","c"],["d","e"]]
	for line in book:
		
		sent = line.rstrip()
		#print('words',sent)

		# here we add an if condition 'if e.isspace()' to keep the space in sentence. 
		# so then later on we can use split(' ') to split words by spaces in between. 
		noPuncWords =  ''.join(e for e in sent if e.isalpha() or e.isspace() or e == '-')
		#print('no punc', noPuncWords)
		sentenses = sentenses + noPuncWords.split(' ')

	for word in sentenses:


		if wordDict.get(word) == None:
			wordDict[word] = 1	
		else:
			wordDict[word] = wordDict[word] + 1

	
	outFile = open('counted_Alice.csv', 'w')    
	for (k,v) in sorted(wordDict.items()):
		outFile.write(k + ',' + str(v) + '\n')
		print(k,v)	

	print(sentenses.count('Alice'))
	print ('key: Alice, occurence: {}'.format(wordDict['Alice']))


	#Question2L find the longest words within the keys. 

	# Method1)
	# keyWordsList = []
	# for (k,v) in sorted(wordDict.items()):
	# 	keyWordsList.append(k)

	# Method2)
	keyWordsList = wordDict.keys()

	print( 'longest key: {}, length: {} '.format(max(keyWordsList, key=len), len(max(keyWordsList, key=len))))