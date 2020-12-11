#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:25:05 2019
@author: abdallah
"""

import sys
import resource

sys.setrecursionlimit(10 ** 6)
#esource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

explored = set()
source_vertex = None
finishing_time = {}
finish = 0
SCCs = []
counter=0 #to hold the index of the current SCC
def DFS_rev(graph , node):
    global finishing_time
    global explored
    global finish
    explored.add(node)
    for edge in graph[node]:
        if edge not in explored:
            DFS_rev(graph , edge)
    finish += 1
    finishing_time[node] = finish

def DFS_loop_rev(graph):
    global explored
    for node in reversed(list(graph.keys())):
        if node not in explored:
            DFS_rev(graph , node)

def DFS(graph , node):
    global SCCs
    global explored
    global source_vertex
    global counter
    explored.add(node)
    for edge in graph[node]:
        if edge not in explored:
            DFS(graph,edge)
            SCCs[counter].add(edge)

def DFS_loop(graph):
    global explored
    global SCCs
    global counter
    explored.clear()
    global finishing_time
    global source_vertex
    f_time = sorted(list(graph.keys()), key = lambda f_time : finishing_time[f_time],reverse=True)
    for node in f_time:
        if node not in explored:
            source_vertex = node
            SCCs.append(set())
            SCCs[counter].add(source_vertex)
            DFS(graph , node)
            counter+=1


graph = {}
rev_graph = {}
with open('2sat6.txt') as f:
    n = int(f.readline())
    data = f.readlines()
    for line in data:
        clause = list(map(int,line[:-1].split(" ")))
        edges = [[-clause[0],clause[1]] , [-clause[1],clause[0]]  ]
        for elements in edges:
            try:
                (graph[elements[0]]).append(elements[1])
            except KeyError:
                graph[(elements[0])] = [elements[1]]
            try:
                (rev_graph[elements[1]]).append(elements[0])
            except KeyError:
                rev_graph[(elements[1])] = [elements[0]]
            if elements[0] not in rev_graph.keys():
                rev_graph[(elements[0])] = []
            if elements[1] not in graph.keys():
                graph[(elements[1])] = []

f.close()




DFS_loop_rev(rev_graph)
DFS_loop(graph)

same_scc = False
for scc in SCCs:
    if(not same_scc):
        for node in scc:
            if -node in scc:
                same_scc = True

if(same_scc):
    print('0')
else:
    print('1')
