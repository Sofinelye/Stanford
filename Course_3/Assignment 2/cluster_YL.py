#####import libraries
from itertools import islice
####Graph class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.parent = n
        self.rank = 0
        self.distances={}
        self.neighbors=list()
    def add_neighbor(self,v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices={}
    edges=[] #[u,v,w]
    #cluster=[]
    #add a vertex to a graph
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            #the points are in separate cluster initially
            #self.cluster.append([vertex.name])
            return True
        else:
            return False
    #add edge to a graph
    def add_edge(self,u,v,w):
        if u in self.vertices and v in self.vertices:
            self.edges.append([u,v,w])
    #union function for node u and v
    def add_neighbors(self,u,v,distance):
        if v in self.vertices and u in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                    value.distances[v]=distance
                if key == v:
                    value.add_neighbor(u)
                    value.distances[u]=distance
    def find(self,v):
        v_p = self.vertices[v].parent
        if v_p == v:
            return v
        return self.find(self.vertices[v_p].parent)
    def union(self,u,v):
        #u's parent & v's parent
        if u in self.vertices and v in self.vertices:
            u_p = self.find(u)
            v_p = self.find(v)
            #rank of u & v's parents
            u_pr = self.vertices[u_p].rank
            v_pr=self.vertices[v_p].rank
        if u_pr==v_pr:
            #increase the rank by 1 for u's parent
            self.vertices[u].rank+=1
            #change the parent of v to u
            self.vertices[v].parent = u
        elif u_pr>v_pr:
            self.vertices[v_p].parent = self.vertices[u_p].parent
        else:
            self.vertices[u_p].parent = self.vertices[v_p].parent

    def KruskalMST(self,num_node,k):
        global T
        T = []    #store the MST
        i = 0
        e = 0
        #initially, the group size equals to the number of nodes
        group_size = num_node
        #print(self.edges)
        #sort edges in increasing order of the weight
        edges_order = sorted(self.edges,key=lambda item:item[2])
        #print(edges_order)
        #while len(T) !=num_node-1: #for MST
        #once the group_size decreases to our desired k,
        #break out of the loop
        while group_size != k:
            u,v,w =edges_order[i]
            u_p = self.find(u)
            v_p = self.find(v)
            #print(u_p,v_p)
            i+=1
            #check if there is a cycle aka if two points have same parent
            if u_p!=v_p:
                e+=1
                #T.append([u,v,w])
                self.union(u_p,v_p)
                #whenever the union happens, the group size decreases by 1
                group_size=group_size-1
        self.max_spacing()
    def max_spacing(self):
        global max_dist
        max_dist = 999999 #set initially distance to a large number
        for v in self.vertices.values():
            for n in v.neighbors:
                #if the neighbor of n is not in the same group of n,
                #check the dist of v-n to see if its the max distance
                n_p = self.find(n)
                v_p = self.find(v.name)
                if n_p != v_p:
                    if v.distances[n]<max_dist:
                        max_dist=v.distances[n]

    def print_MST(self):
        global max_dist
        print(max_dist)
        

#####load file
#desired k-clusters
k=4
with open ('_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt') as f:
#with open ('cluster1_test.txt') as f:
    for line in islice(f,0,1):
        num_node = int(line)
        g=Graph()
    for i in range(1,num_node+1):
        g.add_vertex(Vertex(i))
    for line in islice(f,0,None):
        u,v,distance = line.split()
        g.add_edge(int(u),int(v),int(distance))
        g.add_neighbors(int(u),int(v),int(distance))
g.KruskalMST(num_node,k)
#g.group(k)
g.print_MST()
