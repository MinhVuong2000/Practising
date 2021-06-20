"""
Problem:
Input:
 
[  1   2   3   4  5 ]
[ 16  17  18  19  6 ]
[ 15  24  25  20  7 ]
[ 14  23  22  21  8 ]
[ 13  12  11  10  9 ]
 
Output:
 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
"""

def spiralOrderMatrix(matrix):
    top = left = 0
    bottom = len(matrix)-1
    right = len(matrix[0])-1

    while True:
        if left > right:
            return
        for i in range (left, right+1):
            print(matrix[top][i], end= " ")
        top += 1
        if top > bottom:
            return
        for i in range (top, bottom+1):
            print(matrix[i][right], end= " ")
        right -= 1
        if left > right:
            return
        for i in range(right, left-1,-1):
            print(matrix[bottom][i], end= " ")
        bottom -= 1
        if top > bottom:
            return
        for i in range (bottom, top-1,-1):
            print(matrix[i][left], end= " ")
        left += 1
        
matrix = [
    [1,2,3],
    [12,13,4],
    [11,14,5],
    [10,15,6],
    [9,8,7],
]
spiralOrderMatrix(matrix)


"""
using recursion
"""
# def printSpiral(mat, top, bottom, left, right):
     
#     if left > right:
#         return
 
#     # print top row
#     for i in range(left, right + 1):
#         print(mat[top][i], end=' ')
 
#     top = top + 1
 
#     if top > bottom:
#         return
 
#     # print right column
#     for i in range(top, bottom + 1):
#         print(mat[i][right], end=' ')
 
#     right = right - 1
 
#     if left > right:
#         return
 
#     # print bottom row
#     for i in range(right, left - 1, -1):
#         print(mat[bottom][i], end=' ')
 
#     bottom = bottom - 1
 
#     if top > bottom:
#         return
 
#     # print left column
#     for i in range(bottom, top - 1, -1):
#         print(mat[i][left], end=' ')
 
#     left = left + 1
 
#     printSpiral(mat, top, bottom, left, right)
# matrix = [
#     [1,2,3],
#     [12,13,4],
#     [11,14,5],
#     [10,15,6],
#     [9,8,7],

# ]
# printSpiral(matrix, 0,4,0,2)