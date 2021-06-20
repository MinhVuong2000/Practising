def diagonalMatrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range (r):
        for j in range(0,r):
            if i-j<0 or j>=c:
                continue
            print(matrix[i-j][j], end=' ')
        print('\n')
    for j in range(1,c):
        for i in range(r-1, -1,-1):
            if j+r-1-i>=c:
                continue
            print(matrix[i][j+r-1-i], end=' ')
        print('\n')

matrix = [
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,10],
    [3,4,5,6,7,8,9,10,11],
    [4,5,6,7,8,9,10,11,12],
    [5,6,7,8,9,10,11,12,13],
]
diagonalMatrix(matrix)