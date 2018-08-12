"""
Write a program that finds the longest substring of unique characters within a string. 
If there is more than one such substring, return the first one.

For example:

'abcdab' returns 'abcd'
'abcdabcde' returns 'abcde'

---- extra

'abcdabefb' = 'cdabef'

input_string[start:end]


"""

def longest_substring(input_string):
    start = 0
    #end = 0
    
    charset = set()
    finalSubstring = ''
    
    print(input_string)

    # handles input is null
    if not input_string:
        return None

    # uses dictionary and enumerator to loop through the input_string by its current index. 
    for curIndex,char in enumerate(input_string[:]):
        
        if curIndex < len(input_string):
        
            if char not in charset:
                charset.add(char)
                finalSubstring = input_string[start:curIndex+1]

            else:                
                
                if finalSubstring[0] == char:
                    finalSubstring = finalSubstring[1:]
                    finalSubstring = finalSubstring + char
                    start = start + 1

                # else:
                #     pass
        
    
    return finalSubstring

def test(inp, expected):
    ret = longest_substring(inp)
    print(ret==expected, inp, expected, '"{}"'.format(ret))


    
    
test('dcba', 'dcba')
test('abcdab', 'abcd')
test('aaaa', 'a')
test('abcdabcde', 'abcde')
test('abcdabefb', 'cdabef')
test(None,None)