strings = "Although Python provides us with many list methods, it is good practice and very instructive to think about how Python functions are implemented."
lst = strings.split()
i = "Python"

#count the number of elements in the lst.
def count(i, lst):
    
    counter = 0
    for element in lst:    
        if element == i:
            counter = counter + 1

    return counter

#check whether i is in the lst or not. 
#This method returns boolean value.
def in_method(i, lst):
    
    exist = False
    for element in lst:
        if element == i:
            exist = True
    
    return exist

# This method generates a reversed list from its original list.
def reverse(lst):
    
    reversedList = []
    for index in range(len(lst)-1, -1, -1):
        reversedList.append(lst[index])
    return reversedList

# index. Have a counter ready and increment by 1 everytime until the if condition is satisfied. 
def index(i,lst):
    
    theIndex = -1
    for element in lst:
        theIndex += 1
        if i == element:
            return theIndex

# insert implementation 1. Using for loop and if statement to insert. 
def insert(i, lst, index=0):
    
    insertedList = []
    for element in lst:
        
        if index == lst.index(element):
            insertedList.append(i)
            
        insertedList.append(element)
        
    return insertedList


# insert implementation 2. Using index number to cut in half. 
def insert2(i, lst, index=0):
    
    first_half_list = lst[0:index]
    second_half_list = lst[index:]
    i = [i]
    return first_half_list + i + second_half_list
    
print(count(i, lst))
print(in_method(i, lst))
print(' '.join(reverse(lst)))
print(index(i,lst))
print(insert("PPython", lst,2))
print(insert2("PPython", lst, 2))


