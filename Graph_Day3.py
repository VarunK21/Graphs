# Detect a Cycle
# Distance of nearest cell having 1 
# Redundant Connections
# Surrounded Regions
# Number of Enclaves
# Number of Distinct Islands
# Bipartite Graph
# Detect cycle in directed graph
# Find Eventual Safe states

from collections import deque
def DetectCycleInUndirected(edges):

    def DFS(adj_list,visited,stack):

        while(len(stack)):

            curr_node=stack[-1]
            stack.pop()
            node=curr_node[0]
            parent=curr_node[1]
            
            for neighbours in adj_list[node]:
                
                if(visited[neighbours]==1 and neighbours!=parent):
                    return [node,neighbours]
               
                elif(visited[neighbours]==0):    
                    stack.append((neighbours,node))
                    visited[neighbours]=1
                    
        return
    
    
    

    def BFS(adj_list,visited,q,bfs_order):

        while(len(q)):

            curr_node=q[0]
            q.popleft()
            node=curr_node[0]
            parent=curr_node[1]
            bfs_order.append(node)
            for neighbours in adj_list[node]:
                
                if(visited[neighbours]==0):    
                    q.append((neighbours,node))
                    visited[neighbours]=1
                
                elif(parent!=neighbours):
                    return [node,neighbours]
               
                    
        return
    
    adj_list={}
    for (a,b) in edges:
        if(adj_list.get(a,0)):
            adj_list[a].append(b)
            # if(adj_list.get(b,0)):
            #     adj_list[b].append(a)
            # else:
            #     adj_list[b]=[a]
                
        else:
            adj_list[a]=[b]
            # if(adj_list.get(b,0)):    
            #     adj_list[b].append(a)
            # else:
            #     adj_list[b]=[a]
                   
    visited=[0 for i in range(0,len(adj_list.keys())+1)]
    print(adj_list)
    stack=deque()
    q=deque()
    for i in list(adj_list.keys()):
        if(visited[i]==0):
            visited[i]=1
            stack.append((i,-1))
            #q.append((i,-1))    
            edge=DFS(adj_list,visited,stack)
            #edge=BFS(adj_list,visited,q,bfs_order)
            if(edge):
                return edge
    
#print(DetectCycleInUndirected([[1,2],[2,3],[3,4],[1,4],[1,5]]))



def DetectCYcleInDirectedGraph(V,adj):

    def DFS(stack,visited,adj_list):
        while(len(stack)):
            curr_node=stack[-1]
            stack.pop()
            node=curr_node[0]
            parent=curr_node[1]
            for neighbours in adj_list[node]:
                if(visited[neighbours]==0):
                    stack.append((neighbours,node))
                    visited[neighbours]=1
                elif(visited[neighbours]==1):
                    return neighbours

        return None
    
    adj_list={}
    for i in range(len(adj)):
        a,b=adj[i]
        if(adj_list.get(a,0)):
            adj_list[a].append(b)
        else:
            adj_list[a]=[b]
    
    
    visited=[0 for i in range(V)]
    stack=deque()
    for i in range(V):
        if(visited[i]==0):
            stack.append((i,-1))
            visited[i]=1
            edge=DFS(stack,visited,adj_list)
            if(edge):
                return 1

    return 0

print(DetectCYcleInDirectedGraph(4,[[2,0],[0,1],[1,3],[3,1],[1,0]]))
