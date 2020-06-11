#####import libraries
import heapq
from itertools import islice

####Graph class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()
        self.distances = {}
        self.cheapest_edge = 99999
        self.status = 'unexplored'

    def add_neighbor(self,v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices={}
    def add_vertex(self,vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_neighbors(self,u,v,distance):
        if v in self.vertices and u in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                    value.distances[v]=distance
                if key == v:
                    value.add_neighbor(u)
                    value.distances[u]=distance
    def print_graph(self):
        for i in self.vertices.values():
            print(i.distances,i.neighbors)
    def MST(self): #prim algorithm
        T = []      #vertices spanned by tree-so-far
        pq = [(0,1)] # start with vertex 1
        total = 0
        while pq:
            current_cost,current_node = heapq.heappop(pq)
            if current_node not in T:
                T.append(current_node)
                total+=current_cost
                for neighbor,cost in self.vertices[current_node].distances.items():
                    if neighbor not in T:
                        heapq.heappush(pq,(cost,neighbor))
        print(total)

####load file
g = Graph()
with open ('_d4f3531eac1d289525141e95a2fea52f_edges.txt') as f:
#with open ('MST_test.txt') as f:
    for line in islice(f,0,1):
        num_node,num_edge = line.split()
        num_node=int(num_node)
        #num_edge= int(num_edge)
        for i in range(1,num_node+1):
            #print(i)
            g.add_vertex(Vertex(i))
    for line in islice(f,0,None):
        u,v,distance = line.split()
        g.add_neighbors(int(u),int(v),int(distance))
g.MST()
#g.print_graph()
