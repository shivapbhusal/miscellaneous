'''
A Python program to calculate a nearest char from a given position of char
Alternative approach.
'''
import math

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

    result_list=[]
    for pos in positions:
        neighbor_list = myDict[thisString[pos]]
        nearest = neighbor_list[0]
        for candidate in neighbor_list:
            if not candidate==pos:
                if abs(pos-candidate) <= abs(pos-nearest):
                    if abs(pos-candidate) == abs(pos-nearest):
                        if candidate<nearest:
                            nearest=candidate
                    else:
                        nearest=candidate
            if nearest==pos:
                nearest=-1
        result_list.append(nearest)

    return result_list



            


print(findNearest('abadea',[2,3]))

