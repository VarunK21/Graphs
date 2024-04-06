
def DFS(graph,node,visited):
  print(visited)
  visited.add(node)
  for neighbours in graph[node]:
    if(neighbours not in visited):
      DFS(graph,neighbours,visited)
  






adj_list={0: [1, 2, 4, 8], 1: [0, 5, 6, 9], 2: [0, 4], 4: [0, 2], 8: [0, 3, 5], 5: [1, 8], 6: [1, 7, 9], 9: [1, 6], 3: [7, 8], 7: [3, 6]}
DFS(adj_list,5,set())


from collections import deque
def BFS(graph,curr_node,visited):
  bfs_order=[]
  q=deque()
  visited[curr_node]=1
  q.push(curr_node)
  while(len(q)):
    popped_element=q[0]
    bfs_order.append(popped_element)
    q.popleft()
    for neighbours in graph[popped_element]:
      if(visited[neighbours]==0):
        q.push(neighbours)


  return bfs_order
      

nodes=6
adj_list={
    
}
visited=[0 for i in range(nodes)]
starting_node=
order=BFS(adj_list,starting_node,visited)
print(order)

def bfsOfGraph(V, adj):
  # code here
  visited=[0 for i in range(V)]
  q=deque()
  q.append(0)
  bfs_order=[]
  visited[0]=1
      
  while(len(q)):
      popped_node=q[0]
      q.popleft()
      bfs_order.append(popped_node)
      for neighbour in adj[popped_node]:
          if(visited[neighbour]==0):
              q.append(neighbour)
              visited[neighbour]=1
          
  return bfs_order

bfsOfGraph(len(nodes),adj_list)


#Function to return a list containing the DFS traversal of the graph.
def dfsOfGraph(V, adj):

  # code here
  
  def DFS(adj,curr_node,visited,dfs_order):
      visited[curr_node]=1
      dfs_order.append(curr_node)
      for neighbour in adj[curr_node]:
          if(visited[neighbour]==0):
              DFS(adj,neighbour,visited,dfs_order)
          
      
  visited=[0 for i in range(V)]
  dfs_order=[]
  for i in range(V):
      if(visited[i]==0):
          dfs_order=DFS(adj,i,visited,dfs_order)
  return dfs_order

print(dfsOfGraph(len(nodes),adj_list))

