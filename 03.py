import heapq


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 1, 'F': 2, 'E': 4},
    'B': {'A': 1,'D': 3},
    'C': {'D': 5, 'E': 1, 'F': 7},
    'D': {'B': 3, 'C': 5},
    'E': {'A': 4, 'C': 1, 'F': 3},
    'F': {'A': 2, 'E': 3, 'C': 7}
}

start = 'F'

print(f"Найкоротші відстані від вершини {start}: {dijkstra(graph, start)}")
