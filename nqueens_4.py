# N-Queens Problem for 4 Queens

n = 4

# Create 4x4 board
board = [[0] * n for _ in range(n)]


# Function to check safe position
def isSafe(row, col):

    # Check column
    for i in range(row):

        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1

    while i >= 0 and j < n:

        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


# Backtracking Function
def solve(row):

    # Base Case
    if row == n:

        print("\nSolution Found:\n")

        for i in board:
            print(i)

        return True

    # Try all columns
    for col in range(n):

        # Check safe position
        if isSafe(row, col):

            # Place queen
            board[row][col] = 1

            # Recursive call
            if solve(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Driver Code
solve(0)


# Time Complexity = O(N!)
# Space Complexity = O(N^2)