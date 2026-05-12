import heapq

def prim(graph,start):
    visited=set()
    min_heap=[(0,start)]
    total_cost=0

    while min_heap:

        weight,node=heapq.heappop(min_heap)

        if node not in visited:

            visited.add(node)

            total_cost+=weight

            print("Visited:",node,"Weight:",weight)

            for neighbor,w in graph[node]:

                if neighbor not in visited:

                    heapq.heappush(min_heap,(w,neighbor))

    print("Total Cost of MST:",total_cost)


graph={
    'A':[('B',2),('C',1)],
    'B':[('A',2),('D',4),('E',2)],
    'C':[('A',1),('F',2)],
    'D':[('B',4)],
    'E':[('B',2),('F',3)],
    'F':[('C',2),('E',3)]
}

prim(graph,'A')

