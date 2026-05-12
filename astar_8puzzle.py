# Assignment No. 2
# A* Algorithm for 8 Puzzle Problem

import heapq

# Goal State
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, -1]]

# Heuristic Function
# Counts number of misplaced tiles
def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):

            # Ignore blank tile
            if state[i][j] != -1 and state[i][j] != goal_state[i][j]:
                count += 1

    return count


# Find Blank Tile Position
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == -1:
                return i, j


# Generate Neighbor States
def get_neighbors(state):

    neighbors = []

    # Blank tile position
    x, y = find_blank(state)

    # Possible moves:
    # Right, Left, Down, Up
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        # Check boundaries
        if 0 <= nx < 3 and 0 <= ny < 3:

            # Create deep copy
            new_state = [row[:] for row in state]

            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


# Convert List to Tuple
# Used for storing in set
def to_tuple(state):

    return tuple(tuple(row) for row in state)


# Print Puzzle State
def print_state(state):

    for row in state:
        print(row)

    print()


# A* Search Algorithm
def astar(start):

    # Priority Queue
    open_list = []

    # Push initial state
    # (f, g, state, path)
    heapq.heappush(
        open_list,
        (heuristic(start), 0, start, [])
    )

    # Visited states
    closed_set = set()

    while open_list:

        # Get state with smallest f value
        f, g, current, path = heapq.heappop(open_list)

        # Goal Check
        if current == goal_state:

            print("\nSolution Found!\n")

            steps = path + [current]

            for i, step in enumerate(steps):

                print("Step", i)
                print_state(step)

            print("Total Moves =", len(steps) - 1)

            return

        # Mark current state visited
        closed_set.add(to_tuple(current))

        # Generate neighbors
        for neighbor in get_neighbors(current):

            # Skip visited states
            if to_tuple(neighbor) in closed_set:
                continue

            # Cost from start
            new_g = g + 1

            # f = g + h
            new_f = new_g + heuristic(neighbor)

            # Add to priority queue
            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, path + [current])
            )

    print("No Solution Found")


# MAIN PROGRAM

start_state = []

print("Enter Start State (use -1 for blank):")

for i in range(3):

    row = list(map(int, input().split()))
    start_state.append(row)

# Run A* Algorithm
astar(start_state)



