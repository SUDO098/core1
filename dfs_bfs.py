# DFS Function
def dfs(visited, graph, node):

    # Check if node is not visited
    if node not in visited:

        # Print current node
        print(node, end=" ")

        # Mark node as visited
        visited.add(node)

        # Visit all neighbours recursively
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# BFS Function
def bfs(visited, graph, node, queue):

    # Mark starting node visited
    visited.add(node)

    # Insert node into queue
    queue.append(node)

    # Continue until queue becomes empty
    while queue:

        # Remove first element from queue
        s = queue.pop(0)

        # Print current node
        print(s, end=" ")

        # Visit all neighbours
        for neighbour in graph[s]:

            # If neighbour not visited
            if neighbour not in visited:

                # Mark visited
                visited.add(neighbour)

                # Add into queue
                queue.append(neighbour)


# Main Function
def main():

    # Set for DFS visited nodes
    visited1 = set()

    # Set for BFS visited nodes
    visited2 = set()

    # Queue for BFS
    queue = []

    # Input number of nodes
    n = int(input("Enter number of nodes : "))

    # Empty graph dictionary
    graph = dict()

    # Input graph
    for i in range(1, n + 1):

        # Number of edges
        edges = int(input("Enter number of edges for node {} : ".format(i)))

        # Create empty adjacency list
        graph[i] = list()

        # Input neighbours
        for j in range(1, edges + 1):

            node = int(input("Enter edge {} for node {} : ".format(j, i)))

            graph[i].append(node)

    # DFS Traversal
    print("The following is DFS")

    dfs(visited1, graph, 1)

    print()

    # BFS Traversal
    print("The following is BFS")

    bfs(visited2, graph, 1, queue)


# Driver Code
if __name__ == "__main__":
    main()

#tc- O(v+e)
#sc- O(v)