"""
change all elements of row i, column j to 0 if exist cell (i,j)=0
Input:
 
[ 1  1  0  1  1 ]
[ 1  1  1  1  1 ]
[ 1  1  1  0  1 ]
[ 1  1  1  1  1 ]
[ 0  1  1  1  1 ]
 
Output:
 
[ 0  0  0  0  0 ]
[ 0  1  0  0  1 ]
[ 0  0  0  0  0 ]
[ 0  1  0  0  1 ]
[ 0  0  0  0  0 ]
"""
def changeMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    change_row=[]
    change_col=[]
    for i in range(row):
        for j in range (col):
            if matrix[i][j]==0:
                change_row.append(i)
                change_col.append(j)
    for i in range(row):
        for j in change_col:
            matrix[i][j] = 0
    for j in range(col):
        for i in change_row:
            matrix[i][j] = 0

matrix = [
    [1,1,0,1,1],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [1,1,1,1,1],
    [0,1,1,1,1],
]
changeMatrix(matrix)
print(matrix)