import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize 
        self.visited = False
        self.previous = None

    def addNeighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight
        # print(self.adjacent)

    def getConnections(self):
        return self.adjacent.keys()

    def get_Vertex_ID(self):
        return self.id
    
    def getWeight(self, neighbour):
        return self.adjacent[neighbour]


class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def addVertex(self, node):
        self.numVertices = self.numVertices+1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        # print(self.vertDictionary)
        return newVertex

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)
        
        self.vertDictionary[frm].addNeighbour(self.vertDictionary[to], cost)
        "for undirected case"
        self.vertDictionary[to].addNeighbour(self.vertDictionary[frm], cost)

    
    def getEdges(self):
        edges = []
        for v in self.vertDictionary.values():
            for w in v.getConnections():
                vid = v.get_Vertex_ID()
                wid = w.get_Vertex_ID()
                edges.append([vid, wid, v.getWeight(w)])
        
        return edges

if __name__ == "__main__":
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')

    G.addEdge('a','e', 4)
    G.addEdge('a','c', 1)
    G.addEdge('c','b', 2)
    G.addEdge('b','e', 4)
    G.addEdge('c','d', 4)
    G.addEdge('d','e', 4)

    print(G.getEdges())
