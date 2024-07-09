class Vertex:
    def __init__(self, node):
        self.id = node
        " Mark all the node unvisited "
        self.visited = False
    
    def get_vertex_ID(self):
        return self.id
    
    def set_vertex_ID(self, id):
        self.id = id
    
    def setVisited(self):
        self.visited = True
    
class Graph:
    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            # print("ID", newVertex.id)
            self.vertices.append(newVertex)
        
    def setVertex(self, vtx, id):
        # print(vtx, id)
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].set_vertex_ID(id)

    def getVertex(self, n):
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].get_vertex_ID():
                return vertxin
        else:
            return -1

    def addEdge(self, frm, to, cost=0):
        if self.getVertex(frm)!=-1 and self.getVertex(to)!=-1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)
        
    def getEdge(self):
        edges = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v]!=-1:
                    vid = self.vertices[v].get_vertex_ID()
                    uid = self.vertices[u].get_vertex_ID()
                    edges.append([vid, uid, self.adjMatrix[u][v]])
        return edges



if __name__ == '__main__':
    G = Graph(6)
    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')
    G.setVertex(5,'f')

    print("Graph data")
    G.addEdge('a','e',10)
    G.addEdge('a','c',20)
    G.addEdge('c','b',30)
    G.addEdge('b','e',40)
    G.addEdge('e','d',50)
    G.addEdge('f','e',60)
    G.printMatrix()
    print(G.getEdge())
