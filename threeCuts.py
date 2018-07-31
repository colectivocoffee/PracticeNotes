import random
import numpy

def cutSimulations(nLoops):
	
	SList = []

	for i in range(nLoops): # used for counting means

		cut = True # able to cut the rope? 
		N = 64 # initial length of the rope
		T = 1 # Iterations starts from 1. 
		a = random.randint(1,(N-1))
		b = random.choice(range(1,a) + range(a+1, N-1)))

		c = N - 1 - a - b
		newN = max(a,b,c)
		print('initial a b c', a, b, c)
		print('new N', newN)


	# while newN >= 5:
	# 	a = randint(1, (newN-1)/2)
 # 		c = newN - 1 - (2*a)
 # 		print('a', 'c', a, c)
		
 # 		newN = max(a,c)
 # 		print('while new N', newN)
 # 		if newN <= 5:
 # 			'stop'
 # 			break

		while cut == True:

			# This method checks the S. If S is equals to 2, it does not met the condition. 
			# Then break the loop.  
			if newN == 2 or newN <= 3:
				cut = False
				print('not satisfied', newN)
				break

			T = T + 1
			print('T is ', T)

			# this step calculates the time where iterator T is 5. 
			# When condition is met, then add final S to the List. 
			if T == 5:
				cut = False
				print('T finally ', T)
				print('appending S to the List', newN)
				SList.append(newN)
#				print('current SList', SList)
				break


			# this step sets a and c. but initially we need to verfiy whether c is valid integer (greater than 0). 
			a = randint(1, (newN-1)/2)

			# checks c value. 
			# if c == 0:
			# 	print('c cannot be 0')
			# 	break

			# when c is valid, calculate value of c. 
			c = newN - 1 - (2*a)
			print('a', 'c', a, c)


			# this step checks the latest N and see if it is less or equals to 3. 
			# If the condition is met, it means that we cannot cut the rope anymore.  
# 			if newN <= 3:
# 				cut = False
# 				print('S', newN)
# #				SList.append(newN)
# 				break

			newN = max(a,c)
			print('current N', newN)

	return numpy.mean(SList)
# 	#return ableToCut / float(cutTimes)

print(cutSimulations(1000))
#print('Probability = {}%'.format(cutSimulations(10)*100.0))  
