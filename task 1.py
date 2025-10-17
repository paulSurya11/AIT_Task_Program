from collections import deque
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':['G'],
    'G':[]
  }
def dfs(city,visited=None):
        if visited is None:
            visited=set()
        visited.add(city)
        print(city,end=' ')
        for neighbor in graph[city]:
            if neighbor not in visited:
                dfs(neighbor,visited)

def bfs_shortest_path(start,goal):
    visited=set()
    queue=deque([[start]])
    if start==goal:
        return[start]
    while queue:
        path=queue.popleft()
        city=path[-1]
        if city not in visited:
            for neighbor in graph[city]:
                new_path=list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
                visited.add(city)
    return None

print("DFS Transversal from A:")
dfs("A")
print("\n\n shortest path from A to G using BFS:")
shortest_path=bfs_shortest_path('A','G')
print("->".join(shortest_path))


