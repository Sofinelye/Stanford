#####import libraries

from itertools import islice
####Graph class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.parent = n
        self.rank = 0

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
    def find(self,v):
        v_p = self.vertices[v].parent
        if v_p == v:
            return v
        return self.find(self.vertices[v_p].parent)
    def union(self,u,v):
        #u's parent & v's parent
        if u in self.vertices and v in self.vertices:
            #u_p = self.find(u)
            #v_p = self.find(v)
            u_p=self.vertices[u].parent
            v_p=self.vertices[v].parent
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

    def KruskalMST(self,num_node):
        global T
        T = []    #store the MST
        i = 0
        e = 0
        #print(self.edges)
        #sort edges in increasing order of the weight
        edges_order = sorted(self.edges,key=lambda item:item[2])
        #print(edges_order)
        while len(T) !=num_node-1:
            u,v,w =edges_order[i]
            u_p = self.find(u)
            v_p = self.find(v)

            #print(u_p,v_p)
            i+=1
            #check if there is a cycle aka if two points have same parent
            if u_p!=v_p:
                e+=1
                T.append([u,v,w])
                self.union(u_p,v_p)
    def print_MST(self):
        global T
        print ("Following are the edges in the constructed MST")
        total=0
        for u,v,weight  in T:
            #print ("%d -- %d == %d" % (u,v,weight))
            total+=weight
        print('total:',total)
        #for v in self.vertices.values():
        #    print(v.name,v.parent)
#####load file
#the actual file to be used
#with open ('_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt') as f:
#the test file same as that of the Prim MST
with open ('_d4f3531eac1d289525141e95a2fea52f_edges.txt') as f:
#with open ('cluster1_test.txt') as f:
    for line in islice(f,0,1):
        num_node = int(line.split()[0])
        g=Graph()
    for i in range(1,num_node+1):
        g.add_vertex(Vertex(i))
    for line in islice(f,0,None):
        u,v,distance = line.split()
        g.add_edge(int(u),int(v),int(distance))


g.KruskalMST(num_node)
g.print_MST()
