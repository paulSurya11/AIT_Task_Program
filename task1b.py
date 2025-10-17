graph = {'5':['3','7'],'3':['2','4'],'4':['8'],'2':[],'7':['8'],'8':[]}

visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-first Search")
dfs(visited,graph,'5')
