# Class for Kruskal's Algorithm
class Graph:
    def __init__(self, vertices, nodes):
        self.V = vertices  # Number of vertices
        self.nodes = nodes  # List of node names
        self.graph = []  # List to store all edges in the format (weight, u, v)

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []
        self.graph.sort()  # Sort edges by weight
        parent = list(range(self.V))
        rank = [0] * self.V

        # Initialize adjacency matrix
        adj_matrix = [[0] * self.V for _ in range(self.V)]

        for w, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((self.nodes[u], self.nodes[v], w))  # Use node labels for output
                adj_matrix[u][v] = w  # Add edge weight to adjacency matrix
                adj_matrix[v][u] = w  # Since the graph is undirected, it's symmetric
                self.union(parent, rank, root_u, root_v)

        total_weight = sum(w for _, _, w in mst)
        
        # Print edges in MST
        print("\nEdges in the MST:")
        for u, v, w in mst:
            print(f"{u} - {v} (weight {w})")
        print("Total weight of the MST:", total_weight)

        # Print the Adjacency Matrix
        print("\nAdjacency Matrix of the MST:")
        for row in adj_matrix:
            print(" ".join(map(str, row)))

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

# Main Menu for Selection Sort and Kruskal's Algorithm
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Selection Sort")
        print("2. Kruskal's Algorithm for MST")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            selection_sort_menu()
        elif choice == '2':
            kruskal_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle Selection Sort input
def selection_sort_menu():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    selection_sort(arr)

# Function to handle Kruskal's Algorithm input
def kruskal_menu():
    print("\n--- Kruskal's Algorithm ---")
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = [input(f"Enter name for node {i+1}: ").strip() for i in range(num_nodes)]
    
    g = Graph(num_nodes, nodes)  # Pass the nodes list to the Graph class
    print("\nEnter the edges (e.g., A B 4 for edge A-B with weight 4):")
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (u v weight): ").split()
        weight = int(weight)
        u_idx = nodes.index(u)
        v_idx = nodes.index(v)
        g.add_edge(u_idx, v_idx, weight)
    
    g.kruskal_mst()

# Start the menu
if __name__ == "__main__":
    menu()
