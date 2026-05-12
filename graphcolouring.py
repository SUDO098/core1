# Number of vertices
V = 4

# Number of colors
m = 3

# Graph using adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Store color assigned to each vertex
colors = [0] * V


# Check whether current color can be assigned
def isSafe(vertex, color):

    for i in range(V):

        # If adjacent vertex has same color
        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


# Backtracking function
def solve(vertex):

    # All vertices colored
    if vertex == V:
        return True

    # Try all colors
    for color in range(1, m + 1):

        if isSafe(vertex, color):

            # Assign color
            colors[vertex] = color

            print(f"Color {color} assigned to Vertex {vertex}")

            # Recursive call
            if solve(vertex + 1):
                return True

            # Backtracking
            print(f"Backtracking from Vertex {vertex}")

            colors[vertex] = 0

    return False


# Start coloring from vertex 0
if solve(0):

    print("\nSolution Found")

    for i in range(V):
        print(f"Vertex {i} ---> Color {colors[i]}")

else:
    print("No Solution Exists")

    # tc and sc = O(v)
    #worst case = O(m^v)