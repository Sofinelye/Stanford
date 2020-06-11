#Travel salesman problem
from itertools import islice
import numpy as np
from tqdm import tqdm
################
class Graph:
    def __init__(self,vertices):
        self.n= vertices #No. of vertices
        self.graph = np.zeros((vertices,2))
    # function to add an edge to graph
    def add_Vertex(self,i,x,y):
        self.graph[i,0] = x # point,x,y coordinates
        self.graph[i,1] = y
    def distance(self,i,j):
        x_i = self.graph[i][0]
        y_i = self.graph[i][1]
        x_j = self.graph[j][0]
        y_j = self.graph[j][1]
        res = (x_i-x_j)**2+(y_i-y_j)**2 #take sqrt if needed
        return res
#########main function
    def TSP(self,un_sorted = True):
        #Sort the x coordinate to speed up the algorithm
        #if needed
        #an_array[numpy.argsort(an_array[:, 1])]
        if un_sorted:
            sort_idx = np.argsort(self.graph[:,0])
        else:
            sort_idx = [i for i in range(self.n)]
        ####### BASE CASE
        not_visited = list(sort_idx)
        visited = [0] #visited row,
                                #starting from point with smallest x
        min_dists = []  #stored the minimum distances
        p2_final=0
        ########RECURRENCE
        for i in tqdm(range(self.n-1)):
            p1 = p2_final
            min_dist = np.inf
            #######
            for p2_current in not_visited:
                if p2_current==0:
                    continue
        #    for p2_current,point2 in enumerate(self.graph,0):
        #    point2 is a list of [x,y]
        ################ since we sort the graph in order of x,
        ################  break if p2_x>min_dist,
        #FASTER
                p2_x = self.graph[p2_current][0]
                p1_x = self.graph[p1][0]
                if (p2_x-p1_x)**2>min_dist:
                    break
        #FASTER
        ################
                current_dist = self.distance(p1,p2_current)
        #In case of a tie, go to the closest city with the lowest index.
                if current_dist<min_dist:
                    min_dist = current_dist
                    p2_final = p2_current
                elif current_dist==min_dist:
                    p2_final = min(p2_final,p2_current)
            ########
            not_visited.remove(p2_final)
            visited.append(p2_final)
            min_dists.append(min_dist)
        #visited=visited[:n]
        ########Add final P1 to starting point to the path
        min_dists=np.sqrt(min_dists[:self.n-1])
        visited = visited[:self.n]
        #print(min_dists,visited)
        ###add the distance from last visited point to the first staring point
        #    print(math.sqrt(i))
        total_path = sum(min_dists)
        #print(total_path)
        j = visited[-1]
        end_to_start = np.sqrt(self.distance(sort_idx[0],j))
        #print(end_to_start)
        total_path+=end_to_start
        print(total_path)
############Load file
with open ('nn.txt') as f:
#with open ('TSP_heuristic_test.txt') as f:
    for line in islice(f,0,1):
        num_node = int(line)
        g=Graph(num_node)
    for line in islice(f,0,None):
        i,x,y = line.split()
        g.add_Vertex(int(i)-1,float(x),float(y))
print("Vertices Loaded")
g.TSP()
