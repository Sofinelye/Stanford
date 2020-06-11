#####import libraries
from itertools import islice
import numpy as np
####Graph class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.weight = None
        self.value = None
class Graph:
    vertices={}
    def __init__(self,n,W):
        self.n = n
        self.W = W
        self.A =np.zeros((W+1,n+1))
    def add_vertex(self,vertex,v,w):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            self.vertices[vertex.name].weight =w
            self.vertices[vertex.name].value=v
            return True
        else:
            return False

    def Knapsack(self):
        #A =np.zeros((self.W+1,self.n+1))
        for i in range(1,self.n+1):
            #print('i:',i)
            for x in range(0,self.W+1):
            #    print('x:',x)
                if  i in self.vertices:
                    w_i = self.vertices[i].weight
                    v_i = self.vertices[i].value
                    if w_i>x:
                        self.A[x,i] = self.A[x,i-1]
                    else:
                        self.A[x,i]=max(self.A[x,i-1],self.A[x-w_i,i-1]+v_i)
    def print_A(self):
        print(self.A[self.W,self.n])

#load file

with open ('_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt') as f:
#with open ('_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt') as f:

#with open ('MST_test.txt') as f:
    for line in islice(f,0,1):
        size,num_item = line.split()
        size = int(size)
        num_item=int(num_item)
        #print(size,num_item)
        g = Graph(num_item,size)
        #num_edge= int(num_edge)
    for i,line in enumerate(islice(f,0,None),1):
        v,w = line.split()
        #print(v,w)
        g.add_vertex(Vertex(i),int(v),int(w))
g.Knapsack()
g.print_A()
