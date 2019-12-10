import maya.cmds as cmds

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

def multiply(values):  
    total=values[0]
    for i in values[1:]:
        total *= i
    print("Mulitplication equals: " + str(total))
    return total  

multiply(values)

#Division

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

Power(values)

#mean

def Mean(values):  
    total=values[0]
    for i in values[1:]:
        total += i / len(values)
    print("The Mean equals: " + str(total))
    return total 

Mean(values)

#median

def Median(values):
    median1 = sorted(values)[len(values) // 2 ]
    median2 = sorted(values)[len(values) // 2 - 1]
    median = (median1 + median2) / 2
    print("The median equals: " + str(median))
    return median
Median(values)

#mode

def Mode(values):
    mode = max(values, key = values.count)
    print("The Mode equals: " + str(mode))
    return mode
Mode(values)
    
#operations

def operationType(operations,values):
    if operations == 0:
        Add((values))

    elif operations == 1:
        Subtract((values))

    elif operations == 2:
        multiply((values))
        
    elif operations == 3:
        Division((values))    
    
    elif operations == 4:
        Mean((values))
        
    elif operations == 5:
        Median((values))
    
    elif operations == 6:
        Mode((values))    
          
    elif operations == 7:
        Mode((values))
    else:
        Power((values))
operationType(0,[2,2,5,4])