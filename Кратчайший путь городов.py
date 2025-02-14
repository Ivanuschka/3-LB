import numpy as np
import matplotlib.pyplot as plt

def dfs(graph, current, target, visited, path, min_path, min_distance, current_distance):
    visited.add(current)
    path.append(current)
    
    if current == target:
        if current_distance < min_distance[0]:
            min_distance[0] = current_distance
            min_path.clear()
            min_path.extend(path)
    else:
        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                dfs(graph, neighbor, target, visited, path, min_path, min_distance, current_distance + distance)
    
    path.pop()
    visited.remove(current)

def find_shortest_path_dfs(graph, start, end):
    visited = set()
    min_path = []
    min_distance = [float('inf')]
    dfs(graph, start, end, visited, [], min_path, min_distance, 0)
    return min_path, min_distance[0]

graph = {
    'Город A': [('Город B', 15), ('Город J', 14)],
    'Город B': [('Город A', 15), ('Город D', 12), ('Город H', 25)],
    'Город C': [('Город A', 10), ('Город D', 8), ('Город E', 20)],
    'Город D': [('Город C', 8), ('Город B', 12), ('Город E', 5), ('Город F', 5), ('Город G', 22)],
    'Город E': [('Город C', 20), ('Город D', 5), ('Город F', 18)],
    'Город F': [('Город E', 18), ('Город D', 5), ('Город G', 7)],
    'Город G': [('Город D', 22), ('Город F', 7), ('Город H', 10)],
    'Город H': [('Город G', 10), ('Город B', 25), ('Город I', 6)],
    'Город I': [('Город H', 6), ('Город J', 8)],
    'Город J': [('Город I', 8), ('Город A', 14)]
}

start_city = 'Город E'
end_city = 'Город I'
shortest_path, shortest_distance = find_shortest_path_dfs(graph, start_city, end_city)

print(f'Кратчайший путь из {start_city} в {end_city}: {" -> ".join(shortest_path)}')
print(f'Общая длина пути: {shortest_distance} км')
