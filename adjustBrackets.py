'''
Python Script to reverse chars inside a bracket.

This is a recursive solution.
'''

def reverse(myList, recent_left_bracket, current):
    '''
    Inputs: A list, start index of left bracket, index of right bracket
    Returns: The same list with chars inside bracket in reversed order. 
    '''
    i = recent_left_bracket+1
    j = current-1
    while (i-j)>1:
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp
        i = i + 1
        j = j-1
    temp = myList[i]
    myList[i] = myList[j]
    myList[j] = temp
    return myList

def reverseParentheses(s):
    '''
    Gets the index of first right parentheses and the most recent left parentheses. 
    The process continues recursively until the string doesn't contain any parentheses.
    '''
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

'''
Tests
'''
print(reverseParentheses("Hello(ab)xyz")) # Should give  Hellobaxyz 
print(reverseParentheses("Hello(ab)(cd)xyz")) # Should give Hellobadcxyz
print(reverseParentheses("Hello(wxy)(a)")) # Should give Helloyxwa
print(reverseParentheses("abc((xyz)(cd))")) #Should give abczyxdc and subsequently abccdxyz
