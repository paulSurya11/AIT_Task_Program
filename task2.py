from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph,s):
    vertex=[]
    for i in range(len(graph)):
        if i!=s:
            vertex.append(i)

    min_path = maxsize
    next_permutation=permutations(vertex)
    
    for i in next_permutation:
        current_pathweight=0
        current_path=[s]
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            current_path.append(j)
            k=j
        current_pathweight+=graph[k][s]
        current_path.append(s)
        if current_pathweight<min_path:
            min_path = current_pathweight
            best_path = current_path
            
    return min_path,best_path

if __name__ == "__main__":
    graph=[[0,10,15,20],
           [10,0,35,25],
           [15,35,0,30],
           [20,25,30,0]]
    s=0
    pathWeight,bestPath = travellingSalesmanProblem(graph,s)
    print(f"Minimum Weigth: {pathWeight}")
    print(f"Best Path: {bestPath}")
