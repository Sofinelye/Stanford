#####import libraries
from itertools import islice
import heapq
import os
####Graph class
class Vertex:
    def __init__(self,n):
        self.name = n
        self.weight = None
        self.right = None
        self.left = None
        self.code=[]
        self.code_len=0

class Graph:
    vertices={} #store the information of the vertices
    #add a vertex to a graph
    heap=[]
    roots=[]
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    #add weight to the vertex
    def add_weight(self,v,w):
        if v in self.vertices:
            self.vertices[v].weight = w

    def make_codes(self,r,current_code):
        if r == None:
            return
        if r in self.vertices:
            ln=self.vertices[r].left
            self.vertices[ln].code = current_code
            rn=self.vertices[r].right
            self.vertices[rn].code = current_code
            make_codes(ln,current_code.append(0))
            make_codes(rn,current_code.append(1))


    def huffman(self):
        #make heap out of the vertices

        for v in self.vertices.values():
            #print(v.weight)
            #build a max heap tree
            heapq.heappush(self.heap,(v.weight,v.name))
        #print(self.heap)
        #heapq._heapify_max(heap) #turn the min heap tree to max heap tree
        #merge nodes a,b to ab
        while len(self.heap)>1:
            a = heapq.heappop(self.heap)[1] #vertex.name
            b = heapq.heappop(self.heap)[1]#vertex.name
            #a_=a.translate({95:None})
            #b_=b.translate({95:None})
            #set up the properties(name,leaf/leaves,and weight)
            #for merged vertex ab
            ab = Vertex(str(a)+"_"+str(b))
            #roots.append(ab)
            #ab = Vertex(str(a)+str(b))
            self.add_vertex(ab)
            self.vertices[ab.name].right = b
            self.vertices[ab.name].left = a
            self.vertices[ab.name].weight = self.vertices[a].weight+self.vertices[b].weight
            #push the new merged vertex to the roots
            self.roots.append(ab.name)
            heapq.heappush(self.heap,(self.vertices[ab.name].weight,self.vertices[ab.name].name))
        #print(self.heap)
        #roots.reverse()
        #print(roots)
    #call make_codes function to make codes,inputs(root,current_code)
        self.make_codes(heapq.heappop(self.heap),[])

        for root in self.roots:
            lst = root.split('_')
            for v in lst:
                if v in self.vertices:
                    self.vertices[v].code_len+=1
        #code_len=[]
        max_len=0
        min_len=9999
        for v in self.vertices.values():
            if v.name not in self.roots:
                #code_len.append(v.code_len)
                if v.code_len>max_len:
                    max_len=v.code_len
                if v.code_len<min_len:
                    min_len=v.code_len

        print(min_len,max_len)
        ###
        #print("code:",self.vertices['100'].code)

#####load file

with open ('huffman.txt') as f:
#with open ('huffman_test.txt') as f:
    for line in islice(f,0,1):
        num_node = int(line)
        g=Graph()
    for i in range(1,num_node+1):
        g.add_vertex(Vertex(str(i)))
    for v,w in enumerate(islice(f,0,None),1):
        g.add_weight(str(v),int(w))
        #print("v,w:",str(v),int(w))
g.huffman()
