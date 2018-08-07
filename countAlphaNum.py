'''
Write a program that allows the user to enter a string. 
It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. 
Case should be ignored.

Please enter a sentence: ThiS is String with Upper and lower case Letters.
6 4
L 1
S 2
T 1
U 1
a 2
c 1
d 1
e 5
g 1
h 2
i 4
l 1
n 2
o 1
p 2
r 4
s 3
t 4
w 2

'''



#sent = input("Please enter a sentence: ")
sent = "ThiS is String with Upper and lower case Letters. 6666"


letterDict = {}

noPuncSpaceSent = ''.join(e for e in sent if e.isalnum())
print(noPuncSpaceSent)
lowered = noPuncSpaceSent.lower()
print(lowered)

for letter in lowered:
    
    # if we cannot find the letter key from dictionary, the default output is None.
    # An alternative way is 'letterDict.get(letter, 0) == 0'
    if letterDict.get(letter) == None: 
        letterDict[letter] = 1
    else: 
        # counter = letterDict[letter] + 1
        # letterDict[letter] = counter

        letterDict[letter] = letterDict[letter] + 1

for (k,v) in sorted(letterDict.items()):
    print(k,v)
    
outFile = open('counted_Alpha_Number.csv', 'w')    
for (k,v) in sorted(letterDict.items()):
	outFile.write(k + ',' + str(v) + '\n')




    