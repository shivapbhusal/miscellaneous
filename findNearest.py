'''
A Python program to calculate a nearest char from a given position of char
'''

def findNearest(thisString, pos):
    thisString=list(thisString)
    char=thisString[pos]
    i = 1
    while ((pos-i)>=0) or ((pos+i)<=len(thisString)):
        if (pos-i)>=0:
            if thisString[pos-i]==char:
                return pos-i

        if (pos+i)<len(thisString):
            if thisString[pos+i]==char:
                return pos+i

        i = i+1

    return -1

print(findNearest('abadea',2))

