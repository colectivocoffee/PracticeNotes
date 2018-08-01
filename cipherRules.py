'''

Write a function that implements a substitution cipher. 
In a substitution cipher one letter is substituted for another to garble the message. 
For example A -> Q, B -> T, C -> G etc. 
your function should take two parameters, the message you want to encrypt, 
and a string that represents the mapping of the 26 letters in the alphabet. 

'''

def cipherRules(inputString, skipNumber):
    
    sentCharList = [c for c in inputString]
    
    convertedList = []
    
    for char in sentCharList:
        
        newChar = chr(ord(char)+skipNumber)
        convertedList.append(newChar)
        
    return ''.join(convertedList)


print(cipherRules(
	'Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for another to garble the message.', 1))