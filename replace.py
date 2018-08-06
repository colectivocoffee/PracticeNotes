'''
Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
'''


def replace(s, old, new):
    
    replacedList = []
    
    if ' ' in s:
        print("handling sentence")
        replacedList = replace_sentence(s,old,new)
        return ' '.join(replacedList)
    
    else:
        print("handling only word")
        replacedList = replace_char_in_word(s,old,new)
        return ''.join(replacedList)
        
        

def replace_char_in_word(s,old,new):
    
    # split the word by dilimeter which is old. 
    # Note: char old will be gone. For example:
    # Word = 'Mississippi', Old = 'iss' , New = 'ISS'
    # After the split, 'Mississippi' will become the list like this: ['M', '', 'ippi']
    # Now we have to join the word by gluing with char new.
    oneWordList = s.split(old)
    replacedCharList = new.join(oneWordList)

    return replacedCharList

# This method utilizes replace_char_in_word method and creates the new words list
def replace_sentence(s,old,new):
    
    wordsList = s.split()    
    replacedWordsList = []

    for word in wordsList:

        newWord = replace_char_in_word(word,old,new)
        replacedWordsList.append(newWord)

    return replacedWordsList

# old method. Using concatenation and indexing. 
# This cannot handle if old and new are more than one occurance of old. 
# For example, if we have omleteom. This will not handle properly. 
def replace_part_char_in_sentence(s,old,new):
    
    wordsList = s.split()
    replacedWordsList = []
    
    for word in wordsList:
        
        replacedWordsList.append(word)
        
        if old in word:
            
            indexOfOld = word.index(old)

            # concatenate word by splitting the word. Remember to skip the old part and replace by new ones. 
            # so the index of second half word is '[indexOfOld + len(old): ]' 
            firstHalfWord = word[0:indexOfOld]
            secondHalfWord = word[indexOfOld+len(old):]
            newWord = firstHalfWord + new + secondHalfWord
            
            replacedWordsList.remove(word)
            replacedWordsList.append(newWord)
    
    return replacedWordsList
        
        


########    
s = "I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!"
s2 = "Mississippi"


old = "am"
new = "om"

old2 = "iss"
new2 = "ISS"

print(replace(s,old,new))
print(replace(s2,old2,new2))
print('old & new', old, new)

