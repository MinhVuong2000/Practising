
def createSpiralMatrix(rows, cols, startVal):
    top = left = 0
    right = cols - 1
    bottom = rows - 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    while True:
        if left>right:
            break
        for i in range (left, right+1):
            matrix[top][i] = startVal
            startVal += 1
        top += 1
        if top>bottom:
            break
        for i in range(top, bottom+1):
            matrix[i][right] = startVal
            startVal += 1
        right -= 1
        if left>right:
            break
        for i in range (right,left-1,-1):
            matrix[bottom][i] = startVal
            startVal += 1
        bottom -= 1
        if top>bottom:
            break
        for i in range(bottom, top-1,-1):
            matrix[i][left] = startVal
            startVal += 1
        left += 1
    return matrix

def createSpiralMatrixfromArray1d(array1d, rows, cols):
    top = left = 0
    right = cols - 1
    bottom = rows - 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    idx = 0
    while True:
        if left>right:
            break
        for i in range (left, right+1):
            matrix[top][i] = array1d[idx]
            idx += 1
        top += 1
        if top>bottom:
            break
        for i in range(top, bottom+1):
            matrix[i][right] = array1d[idx]
            idx += 1
        right -= 1
        if left>right:
            break
        for i in range (right,left-1,-1):
            matrix[bottom][i] = array1d[idx]
            idx += 1
        bottom -= 1
        if top>bottom:
            break
        for i in range(bottom, top-1,-1):
            matrix[i][left] = array1d[idx]
            idx += 1
        left += 1
    return matrix

array1d = range(1,21)
print(createSpiralMatrixfromArray1d(array1d,4,5))

print(createSpiralMatrix(4,5,1))