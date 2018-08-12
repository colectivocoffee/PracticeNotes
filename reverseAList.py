'''
Write a recursive function to reverse a list.
'''


def reverseList(numList):

	if numList == None:
		return None
	elif len(numList) == 1:
		return numList 	
	else: 
		return [numList[-1]] + reverseList(numList[:-1])




def test(inp, expected):

    result = reverseList(inp)
    print(result==expected, inp, expected, '"{}"'.format(str(result)))


test([1,2,3,4], [4,3,2,1])
test([-1,-2,-3,-4],[-4,-3,-2,-1])
test(None,None)