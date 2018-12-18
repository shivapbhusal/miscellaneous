'''
Python Program to merge the sorted arrays
'''

def merge(array1, array2):
    m = len(array1)
    n = len(array2)

    if m == 0:
        return array2

    if m == 0:
        return array1

    array1.append(float('inf'))
    array2.append(float('inf'))

    i = 0
    j = 0
    result = []

    while (i<m or j <n):
        if array1[i]<=array2[j] or j ==n:
            result.append(array1[i])
            i = i + 1
        else:
            result.append(array2[j])
            j = j + 1

    return result

result = merge([1,2,10],[2,3,5])

print(result)



