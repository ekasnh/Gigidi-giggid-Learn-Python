import csv
import heapq
from collections import defaultdict

def load_graph_from_csv(file_path):
    """
    Loads a graph from a CSV file. The CSV file should have columns: source, destination, weight.
    """
    graph = defaultdict(list)
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row['source']
            destination = row['destination']
            weight = int(row['weight'])
            graph[source].append((destination, weight))
            graph[destination].append((source, weight))  # Assuming undirected graph
    return graph

def dijkstra(graph, start):
    """
    Performs Dijkstra's algorithm on the graph from the start node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    # Specify the CSV file path
    csv_file_path = 'graph_data.csv'  # Replace with your CSV file path
    
    # Load the graph from the CSV file
    graph = load_graph_from_csv(csv_file_path)
    
    # Get the start node from the user
    start_node = input("Enter the start node: ")
    
    # Perform Dijkstra's algorithm
    distances = dijkstra(graph, start_node)
    
    # Display the shortest distances from the start node
    print(f"Shortest distances from {start_node}:")
    for node, distance in distances.items():
        print(f"{node}: {distance}")

if __name__ == "__main__":
    main()

