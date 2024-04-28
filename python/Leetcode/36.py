""" Sudoku problem """

from collections import defaultdict
import numpy as np 
grid = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def checkInvalid(grid):

    tempgrid = np.array(grid)

    print("1")
    for i in range(9):
        hash = defaultdict(int)
        for j in range(9):
            if grid[i][j]!='.':
                hash[grid[i][j]]+=1
                if hash[grid[i][j]] > 1:
                    print(hash)
                    return False

    print("2")
    for i in range(9):
        hash = defaultdict(int)
        for j in range(9):
            if grid[j][i]!='.':
                hash[grid[j][i]]+=1
                if hash[grid[j][i]] > 1:
                    return False

    print("3")
    for i in range(0,9,3):
        for j in range(0,9,3):
            """ Extract 3*3 matrix"""

            submatrix = [row[j:j+3] for row in grid[i:i+3]]
            # print(submatrix)
            templist = []
            for rowi in range(len(submatrix)):
                templist.extend(submatrix[rowi])

            """ Second approach"""
            # temp =  tempgrid[j:j+3, i:i+3]
            # templist = temp.flatten()

            hash = defaultdict(int)
            for hashteq in templist:
                if hashteq!='.':
                    hash[hashteq]+=1
                    if hash[hashteq] > 1:
                        return False
        
    return True
                
output = checkInvalid(grid)
print(output)