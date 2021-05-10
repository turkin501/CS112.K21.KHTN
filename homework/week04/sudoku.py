def print_matrix(matrix):
    for i in range(9):
            print(matrix[i])
 
def find_empty(matrix, l):
    for row in range(9):
        for col in range(9):
            if(matrix[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
 
def checkRow(matrix, row, num):
    for i in range(9):
        if(matrix[row][i] == num):
            return True
    return False
 
def checkCol(matrix, col, num):
    for i in range(9):
        if(matrix[i][col] == num):
            return True
    return False
 
def checkSquare(matrix, row, col, num):
    for i in range(3):
        for j in range(3):
            if(matrix[i + row][j + col] == num):
                return True
    return False
 
def checking(matrix, row, col, num):
    return not checkRow(matrix, row, num) and not checkCol(matrix, col, num) and not checkSquare(matrix, row - row % 3,col - col % 3, num)
def solve_sudoku(matrix):
    l =[0, 0]
    if(not find_empty(matrix, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if(checking(matrix,row, col, num)):
            matrix[row][col]= num
            if(solve_sudoku(matrix)):
                return True
            matrix[row][col] = 0
    return False
    
    
#matrix  = [
#    [7,8,0,4,0,0,1,1,0],
#    [6,0,0,0,7,5,0,0,9],
#    [0,0,0,6,0,1,0,7,8],
#    [0,0,7,0,4,0,2,6,0],
#    [0,0,1,0,5,0,9,3,0],
#    [9,0,4,0,6,0,0,0,5],
#    [0,7,0,3,0,0,0,1,2],
#    [1,2,0,0,0,7,4,0,0],
#    [0,4,9,2,0,6,0,0,7]
#]

for i in range(9):   
    rows = []
    for j in input().strip().split():
        rows.append(int(j))
    matrix.append(rows)
    
solve_sudoku(matrix)
flag = True
for i in range(9):
    for j in range(9):
        for k in range(9):
            if(checking(matrix,i,j,k) == False):
                flag = False 
                break
if(flag):
    print_matrix(matrix)
else:
    print(-1)
            

