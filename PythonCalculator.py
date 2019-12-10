import maya.cmds as cmds


values = [5,3,1,7]

#Addition

def Add(values):  
    total=values[0]
    for i in values[1:]:
        total += i
    print("Addition equals: " + str(total))
    return total 

Add(values)

#Subtraction

def Subtract(values):  
    total=values[0]
    for i in values[1:]:
        total -= i
    print("Subtraction equals: " + str(total)) 
    return total 

Subtract(values)

#Multiplication


values = [5,3,1,7]

def multiply(values):  
    total=values[0]
    for i in values[1:]:
        total *= i
    print("Mulitplication equals: " + str(total))
    return total  

multiply(values)



#Division

values = [6,3]
def Division(values):  
    total=values[0]
    for i in values[1:]:
        if i != 0:
            total /= i
    print("Division equals: " + str(total)) 
    return total 

Division(values)

#Power

def Power(values):
    pow=values[0] ** values[1]
    
    print(pow)    

Power([10,2,8])

#mean

def Mean(values):  
    total=values[0]
    for i in values[1:]:
        total += i / len(values)
    print("The Mean equals: " + str(total))
    return total 

Mean([2,53,5,2])

#median

def Median(values):
    median1 = sorted(values)[len(values) // 2 ]
    median2 = sorted(values)[len(values) // 2 - 1]
    median = (median1 + median2) / 2
    print("The median equals: " + str(median))
    return median
Median([2,54,7,3,7,1,6,13,7])

#mode

def Mode(values):
    mode = max(values, key = values.count)
    print("The Mode equals: " + str(mode))
    return mode
Mode([2,2,2,2,5,7,2,7,4,5,7,8,9,76,34,1,5])
    
#operations

def operationType(operations,values):
    if operations == 0:
        Add()

    elif operations == 1:
        Sub()

    elif operations == 2:
        Mult()
        
    elif operations == 3:
        Divis()    
    
    elif operations == 4:
        Mean()
        
    elif operations == 5:
        Median()
          
    elif operations == 6:
        Mode()
    else:
        Power()
operationType(1[2,5,4])

