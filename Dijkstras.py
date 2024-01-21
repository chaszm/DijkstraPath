import heapq  



def dijkstra(graph, start):
   
    dist = {node: float('inf') for node in graph}   # set to inf


    dist[start] = 0         #distance from start vertex
    priority_queue = [(0, start)]



    while priority_queue:
        # node with smallest distance from starting node
        current_distance, current_node = heapq.heappop(priority_queue)

        # if already visited node, skip (already have shortest path)
        if current_distance > dist[current_node]:
            continue




        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight    # check nodes, add corresponding distances

           # with new calculated distance, compare 
           # if there is shorter path, update dist to shorter value
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) # push node

    return dist





# Given Graph on Assignment:
graph = {
    'A': {'B': 12, 'C': 3, 'E': 6},
    'B': {'A': 12, 'C': 15, 'D': 5, 'B': 5},
    'C': {'A': 3, 'B': 15, 'F': 18},
    'D': {'B': 5, 'F': 4, 'H': 19},
    'E': {'A': 6, 'B': 5, 'G': 22},
    'F': {'C': 18, 'D': 4, 'H': 10},
    'G': {'E': 22, 'H': 4},
    'H': {'D': 19, 'F': 10, 'G': 4}
}

start_node = 'A'



shortest_path = dijkstra(graph, start_node)
print("Shortest Distance to each node from A:")
print(" ")
print(shortest_path)