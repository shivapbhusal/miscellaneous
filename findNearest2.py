'''
A Python program to calculate a nearest char from a given position of char
Alternative approach.
'''

def findNearest(thisString, positions):
    thisString=list(thisString)
    myDict=dict()
    for pos in positions:
        myDict[thisString[pos]]=[]
    print(myDict)

    for i in range(len(thisString)):
        if thisString[i] in myDict:
            myDict[thisString[i]].append(i)
    print(myDict)

    for pos in positions:
        neighbor_list = myDict[thisString[pos]]
        for candidates in neighbor_list:


print(findNearest('abadea',[2,3]))

