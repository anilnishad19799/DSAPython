""" Search 2D matrix """

def search2DMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    block = 0
    blockflag = False
    for index, i in enumerate(matrix):
        if target == i[0]:
            return True
        
        if target < i[0]:
            block = index-1
            blockflag = True
            break
    
    if not blockflag:
        block = m-1

    l = 0
    r = n

    while l!=r:
        mid = (l+r) // 2
        if target == matrix[block][mid]:
            return True
        elif target < matrix[block][mid]:
            r = mid
        else:
            l = mid+1

    return False

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 30
output = search2DMatrix(matrix, target)
print(output)