'''
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. for example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. for example: madam i’m adam is a palindrome. Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota

'''


# from test import testEqual

def removeWhite(s):
    
    s = ''.join(c.lower() for c in s if c.isalpha())
    print(s)
    return s

def isPal(s):
    
    # this handles when input is an empty string ''
    if len(s) == 0:
        return True
        
    if reverseString(s) == s:
        return True
    else: 
        return False

def reverseString(s):

    if len(s) == 1:
        return s
    else:
        return s[-1] + reverseString(s[:-1])


# testEqual(isPal(removeWhite("x")),True)
# testEqual(isPal(removeWhite("radar")),True)
# testEqual(isPal(removeWhite("hello")),False)
# testEqual(isPal(removeWhite("")),True)
# testEqual(isPal(removeWhite("hannah")),True)
# testEqual(isPal(removeWhite("madam i'm adam")),True)

print('Answer x', isPal(removeWhite("x")))     #True
print('Answer radar', isPal(removeWhite("radar"))) #True
print('Answer hello', isPal(removeWhite("hello"))) #False
print('Answer ''', isPal(removeWhite("")))      #True
print('Answer hannah', isPal(removeWhite("hannah")))#True
print('Answer madam im madam', isPal(removeWhite("madam i'm adam")))#True


print('Answer Go hang a salami; I’m a lasagna hog.', isPal(removeWhite("Go hang a salami; I’m a lasagna hog.")))