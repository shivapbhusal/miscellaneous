'''
Python Script to reverse chars inside a bracket.
'''

def reverse(myList, recent_left_bracket, current):
    '''
        check this.
    '''
    i = recent_left_bracket
    j = current
    while (i!=j):
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp
        i = i + 1
        j = j-1
    return myList

def reverseParentheses(s):
    if "(" not in s or ")" not in s:
        return s
    else:
        myList= list(s)
        recent_left_bracket = 0
        i =0
        while myList[i]!=")":
            # print(myList[i])
            if myList[i] =="(":
                recent_left_bracket = i
            i = i+1
    reverse(myList, recent_left_bracket, i)
    del myList[i]
    del myList[recent_left_bracket]
    return reverseParentheses("".join(map(str, myList)))
    i = i+1

print(reverseParentheses("Hello((abc)(One)xyz)"))
