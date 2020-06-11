from collections import defaultdict
from tqdm import tqdm

class Graph:
    def __init__ (self,g,num_nodes,order):
        self.n = num_nodes
        self.g = g
        self.explored = [False]*num_nodes #index is vertex-1, value is status
        self.leaders = [0]*num_nodes #index is leader-1, value is the size
        self.finish = {} #finish time
        self.order = order #for 2nd dfs on original graph only

    ################################################
    ######dfs_loop1 function is for or r_g only
    def dfs_loop1(self): # s denotes the first explored node
        global t,s
        t = 0
        s = None
        print("first loop")
        for i in range(self.n,0,-1):
            #if i not in self.explored:
            if self.explored[i-1]==False:
                s = i
                self.dfs(i)


    ################################################
    ######dfs_loop2 function is for or g only
    def dfs_loop2(self):
        global t,s
        t = 0
        s = None
        print("second loop")
        for i in self.order:
            if self.explored[i-1]==False:
                s = i
                self.dfs(i)

    ################################################
    #########recursive dfs function
    def dfs(self,i):
        global t,s
        #self.explored.append(i)
        self.leaders[s-1]+=1
        self.explored[i-1]=True
        for neighbor in self.g[i]:
            #if neighbor not in self.explored:
            if self.explored[neighbor-1] ==False:
                self.dfs(neighbor)
        t+=1
        self.finish[i] = t

    ##############

    def get_finish(self):
        order = []
        for i in self.finish.keys():
            order.append(i)
        #print(order)
        order.reverse()
        #print(order)
        return order

    def print_scc(self,c):
        #print ("finish",self.finish)
        #print("explored:",self.explored)
        #print("leaders",self.leaders)
        #######
        #largest_count = []
        self.leaders.sort(reverse=True)
        #scc_count = [[x,l.count(x)] for x in set(l)]

        #####or use dict
        print(self.leaders[:c])

#####Load file
print("Load file")
g = defaultdict(list)
r_g = defaultdict(list)
#num_nodes= 875815
num_nodes = 9
with open('dfs_test.txt','r') as f:
#with open('SCC.txt','r') as f:
    for line in tqdm(f):
        u,v = line.split()
        u,v = int(u),int(v)
        g[u].append(v)
        r_g[v].append(u)
#print(g,r_g)
r_g_dfs=Graph(r_g,num_nodes,[])
r_g_dfs.dfs_loop1()
order = r_g_dfs.get_finish()
g = Graph(g,num_nodes,order)
g.dfs_loop2()
g.print_scc(5)
#######
