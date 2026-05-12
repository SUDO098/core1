from queue import PriorityQueue

# Graph representation
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}


def astar(start, goal):

    # Priority Queue
    open_set = PriorityQueue()

    # Add starting node
    open_set.put((0, start))

    # Cost from start node
    g_cost = {start: 0}

    # Parent nodes
    parent = {start: None}

    while not open_set.empty():

        # Get node with minimum cost
        current = open_set.get()[1]

        print("Visiting Node:", current)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path

        # Check neighbours
        for neighbour in graph[current]:

            # Calculate new cost
            new_cost = g_cost[current] + graph[current][neighbour]

            # If better path found
            if neighbour not in g_cost or new_cost < g_cost[neighbour]:

                g_cost[neighbour] = new_cost

                # f(n) = g(n) + h(n)
                f_cost = new_cost + heuristic[neighbour]

                open_set.put((f_cost, neighbour))

                parent[neighbour] = current

    return None


# Driver Code
start = 'A'
goal = 'G'

path = astar(start, goal)

print("\nShortest Path:")
print(path)


#sc - bc - O(log V)
#sc - wc - O(E log V)
#tc - O(V)