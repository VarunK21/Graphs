# Adjacency Matrix and Adjacency List
def AdjacencyMatrixList(nodes,edges):

  n=len(nodes)
  #Adjacency Matrix
  adj_mat=[[0 for i in range(n)] for j in range(n)]
  for (u,v) in edges:
    adj_mat[u][v]=1
    adj_mat[v][u]=1
  
  print(adj_mat)

  adj_list={}

  for (u,v) in edges:
    print(u,v)
    if(adj_list.get(u,0)):
      adj_list[u].append(v)
    if(adj_list.get(u,0)==0):
      adj_list[u]=[v]
    if(adj_list.get(v,0)):
      adj_list[v].append(u)
    if(adj_list.get(v,0)==0):
      adj_list[v]=[u]

  print(adj_list)


n,m=[int(x) for x in input().split(" ")]
edges=[]
for i in range(m):
  a,b=[int(x) for x in input().split(" ")]
  edges.append(tuple([a,b]))
nodes=[i for i in range(n)]

AdjacencyMatrixList(nodes,edges)

