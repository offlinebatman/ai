import heapq

class Graph:
    def __init__(self, V): 
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))


    def shortestPath(self, src):
        pq = []
        heapq.heappush(pq, (0, src))
        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)
            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    g = Graph(V)

    E = int(input("Enter the number of edges: "))
    for _ in range(E):
        u, v, w = map(int, input("Enter the edge (u, v) and its weight w: ").split())
        g.addEdge(u, v, w)

    src = int(input("Enter the source vertex: "))
    g.shortestPath(src)
