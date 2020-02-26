import random

def getRandomArray(n):
    returnArray=[]
    while len(returnArray)!=n:
        randomNum=random.randint(1,n+1)
        if randomNum not in returnArray:
            returnArray.append(randomNum)
    return returnArray

print(getRandomArray(10))