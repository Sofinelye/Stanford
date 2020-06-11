#using 1 (the first vertex) as the source vertex
# return the distance from 1 to the following nodes:
#7,37,59,82,99,115,133,165,188,197
import heapq

class Vertex:
    def __init__(self,n):
        self.name = n
        #self.finish = 0
        #self.status = 'unexplored' #unexplored
        self.neighbors = list()
        self.distances = {}
        self.dts =1000000 #distance to source
        #self.discovery = 0
    def add_neighbor(self,n):
        nset = set(self.neighbors)
        if n not in nset:
            self.neighbors.append(n)

class Graph:
    def __init__(self):
        self.vertices = {}
    #    self.nodes = set()
    # Using a Python dictionary to act as an adjacency list
    #visited is a dict to record the visited order of the vertices
    def add_vertex(self,vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_neighbors(self,u,v):
        #directed lsit, u(tail) to v(head), u is a str input, v is a list of str
        if v in self.vertices and u in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
    def add_distance(self,distance_list):
        v = int(distance_list[0])
        if v in self.vertices:
            for i in distance_list[1:]:
                node,distance = i.split(',')
                #print(v,node,distance)
                node = int(node)
                if node not in self.vertices[v].distances:
                    self.vertices[v].distances[node] = int(distance)
        #    print(v,self.vertices[v].distances)
    def dijsktra(self,s):

        X = [s]
        self.vertices[s].dts=0
        #B[s] = [] #computed shortest path
        #V = list(self.vertices.keys())
        pq = [(0,s)]
        #record_distance = 1000000
        ###Main dfs_loop
        while pq:
            current_distance,current_vertex = heapq.heappop(pq)
            if current_distance>self.vertices[current_vertex].dts:
                continue
            for neighbor,weight in self.vertices[current_vertex].distances.items():
                distance = current_distance+weight
                if distance < self.vertices[neighbor].dts:
                    self.vertices[neighbor].dts = distance
                    heapq.heappush(pq,(distance,neighbor))
        for i in [7,37,59,82,99,115,133,165,188,197]:
            print(self.vertices[i].dts)


################load file
num_nodes = 200
g = Graph()
for i in range(1,num_nodes+1):
    v = Vertex(i)
    g.add_vertex(v)
with open('dijkstraData.txt') as f:
    for line in f:
        distance_list = line.split()
        #print(distance_list[0])
        g.add_distance(distance_list)
f.close()

g.dijsktra(1)
