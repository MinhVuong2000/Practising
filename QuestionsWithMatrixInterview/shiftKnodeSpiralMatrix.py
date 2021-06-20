def shiftKnodeSpiralMatrix(matrix,k):
    top = left = 0
    bottom = len(matrix)-1
    right = len(matrix[0])-1
    start = matrix[0][0]
    end = matrix[0][0] + (right+1)*(bottom+1) - 1
    begin = end - k + 1

    while True:
        if left > right:
            return
        for i in range (left, right+1):
            matrix[top][i] = begin%(end+1) + start*begin//(end+1)
            begin+=1
        top += 1
        if top > bottom:
            return
        for i in range (top, bottom+1):
            matrix[i][right] = begin%(end+1) + start*begin//(end+1)
            begin+=1
        right -= 1
        if left > right:
            return
        for i in range(right, left-1,-1):
            matrix[bottom][i] = begin%(end+1) + start*begin//(end+1)
            begin+=1
        bottom -= 1
        if top > bottom:
            return
        for i in range (bottom, top-1,-1):
            matrix[i][left] = begin%(end+1) + start*begin//(end+1)
            begin+=1
        left += 1
        
matrix = [
    [1,2,3],
    [12,13,4],
    [11,14,5],
    [10,15,6],
    [9,8,7],
]
shiftKnodeSpiralMatrix(matrix,2)
print(matrix)