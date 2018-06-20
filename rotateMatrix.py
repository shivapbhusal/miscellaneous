'''
A Python script to rotate an (N*N) Matrix  by 90 degree.
The matrix is given in the form of a nested list. 
Time Complexity: O(N^2), where N is the number of rows or columns.
Space Complexity: O(N) 
'''

def  rotateMatrix (matrix):
    m = len(matrix)
    result = []
    '''
    First create a matrix and initialize each elements with 0.
    '''
    for i in range(m):
        temp = []
        for j in range(m):
            temp.append(0)
        result.append(temp)

    i = 0
    m = 0
    while (i<=2):
        j = 0
        n = 2
        while (j<=2):
            result[i][j] =matrix[n][m]
            j = j+1
            n = n-1
        m = m+1
        i=i+1
    
    return result

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))


            

