'''
Write a function called rot13 that uses the Caesar cipher to encrypt a message. 
The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to ‘its right’ in the alphabet. 
So for example the letter a becomes the letter n. 
If a letter is past the middle of the alphabet then the counting wraps around to the letter a again, so n becomes a, o becomes b and so on. 
Hint: Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic.

'''


import string

def rot13(mess):
    
    #sentCharList = [c for c in mess]
    convertedList = []
    
    for char in mess:
        
        if char in string.ascii_lowercase[0:13] or char in string.ascii_uppercase[0:13]:
            newChar = chr(ord(char)+13)
            convertedList.append(newChar)
        elif char in string.ascii_lowercase[13:] or char in string.ascii_uppercase[13:]:
            newChar = chr(ord(char)-13)
            convertedList.append(newChar)
        
    return ''.join(convertedList)



print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('Since rot13 is symmetric you should see this message')))