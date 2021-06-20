"""
height means from top to this position, there are how many '1'
left means at current position, what is the index of left bound of the rectangle with height[j]. 0 means at this position, no rectangle.
right means the right bound index of this rectangle. 'n' means no rectangle.
"""
def maximalRectangle(matrix):
        if not matrix:
            return 
        n = len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        res = 0
        
        for row in matrix:
            # calculate right
            currentRight = n      
            for i in range(n-1,-1,-1):
                if row[i] == 1:
                    right[i] = min(right[i],currentRight)
                else:
                    right[i] = n 
                    currentRight = i
            
            currentLeft = 0
            for i in range(n):
                # calculate height
                height[i] = height[i]+1 if row[i] == 1 else 0
                # calculate left
                if row[i] == 1:
                    left[i] = max(left[i],currentLeft)
                else:
                    left[i] = 0
                    currentLeft = i+1
                # calculate Rectangle
                res = max(res,height[i]*(right[i]-left[i]))
            print(left)
            print(right)
            print(height)
            print('\n')
        return res

# Driver Code
if __name__ == '__main__':
    A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    print(maximalRectangle(A))
 