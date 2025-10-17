import math 
import random 
locations = { 
    'Start': (0, 0), 
    'Item1': (2, 3), 
    'Item2': (5, 4), 
    'Item3': (1, 8), 
    'Item4': (7, 2) 
} 
def euclidean(p1, p2): 
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) 
def calculate_total_distance(path): 
    total = 0 
    current = locations['Start'] 
    for place in path: 
        total += euclidean(current, locations[place]) 
        current = locations[place] 
    total += euclidean(current, locations['Start'])  
    return round(total, 2) 
def generate_neighbors(path): 
    neighbors = [] 
    for i in range(len(path)): 
        for j in range(i + 1, len(path)): 
            neighbor = path.copy() 
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i] 
            neighbors.append(neighbor) 
    return neighbors 
def hill_climb(start_path): 
    current_path = start_path 
    current_cost = calculate_total_distance(current_path) 
    iterations = 0 
    while True: 
        neighbors = generate_neighbors(current_path) 
        next_path = current_path 
        next_cost = current_cost 
        for neighbor in neighbors: 
            cost = calculate_total_distance(neighbor) 
            if cost < next_cost: 
                next_path = neighbor 
                next_cost = cost 
        if next_cost == current_cost: 
            break  
        current_path = next_path 
        current_cost = next_cost 
        iterations += 1 
    return current_path, current_cost, iterations 
item_keys = list(locations.keys())[1:]  
random_start = random.sample(item_keys, len(item_keys)) 
print("Initial random path:", ' -> '.join(random_start)) 
initial_cost = calculate_total_distance(random_start) 
print("Initial total distance:", initial_cost) 
best_path, best_cost, steps = hill_climb(random_start) 
print("\nOptimized path:", ' -> '.join(best_path)) 
print("Optimized total distance:", best_cost) 
print("Iterations:", steps) 
