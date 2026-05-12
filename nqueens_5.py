n=5
board=[[0]*n for _ in range(n)]

def isSafe(row,col):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        
        i-=1
        j-=1

    
    i,j=row-1,col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        
        i-=1
        j+=1

    return True

def solve(row):

    if row==n:
        print("\nSolution")
        for i in board:
            print(i)
        return True
    
    for col in range(n):
        if isSafe(row,col):
            board[row][col]=1

            if solve(row+1):
                return True
            
            board[row][col]=0

    return False

solve(0)



#worst case tc = O(n!)
#best case =O(n)
#sc=O{n^2}