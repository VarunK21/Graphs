# Number of Provinces
# Number of Islands
# Flood Fill AAlgorithm
# Rotten Oranges
from collections import deque

def NumberOfProvinces(arr):

    def dfs(stack,visited,adj_list):
        
        while(len(stack)):
            curr_node=stack[-1]
            stack.pop()
            for neighbours in adj_list[curr_node]:
                if(visited[neighbours]==0):
                    stack.append(neighbours)
                    visited[neighbours]=1

        


    visited=[0 for i in range(len(arr))]
    
    # Change Adj Matrix to Adj List
    adj_list={}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j]==1):    
                if(adj_list.get(i,0)):    
                    adj_list[i].append(j)
                else:
                    adj_list[i]=[j]
    cnt=0
    stack=deque()
    for i in range(len(arr)):
        if(visited[i]==0):
            stack.append(i)
            dfs(stack,visited,adj_list)
            cnt+=1
    

    return cnt

arr=[[1,1,0],[1,1,0],[0,0,1]]
print(NumberOfProvinces(arr))


def NumberOfIslands(arr):
    
    def dfs(visited,stack):

        while(len(stack)):
            curr_node=stack[-1]
            curr_x=curr_node[0]
            curr_y=curr_node[1]
            stack.pop()
            for (dir_x,dir_y) in [(-1,0),(0,-1),(0,1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
                new_x=curr_x+dir_x
                new_y=curr_y+dir_y

                if(new_x>=0 and new_y>=0 and new_x<len(arr) and new_y<len(arr[0])):
                    if(visited[new_x][new_y]==0 and arr[new_x][new_y]=="1"):
                        print(new_x,new_y)
                        stack.append((new_x,new_y))
                        visited[new_x][new_y]=1

    visited=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]

    cnt=0
    stack=deque()

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(visited[i][j]==0 and arr[i][j]=="1"):
                stack.append((i,j))
                visited[i][j]=1
                dfs(visited,stack)
                cnt+=1

    return cnt

arr=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print("noi",NumberOfIslands(arr))

def FloodFill(arr,x,y,c):
    prev_c=arr[x][y]
    directions=[(-1,0),(0,-1),(1,0),(0,1)]
    visited=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    q=deque()
    q.append((x,y))
    while(len(q)):
        curr_x,curr_y=q[0][0],q[0][1]
        visited[curr_x][curr_y]=1
        arr[curr_x][curr_y]=c
        q.popleft()
        for (dir_x,dir_y) in directions:
            new_x,new_y=curr_x+dir_x,curr_y+dir_y
            if(new_x>=0 and new_x<len(arr) and new_y>=0 and new_y<len(arr[0])):
                
                if(arr[new_x][new_y]==prev_c and visited[new_x][new_y]==0):    
                    q.append((new_x,new_y))

    return arr

n,m=4,5
arr=[[1],[1]]
#arr=[[2, 1, 2 ,1, 3],[2, 3 ,3 ,3 ,2],[2, 3 ,1 ,3 ,2],[1, 2 ,3 ,2, 2]]
x,y,c=0,0,1
print(FloodFill(arr,x,y,c))


def RottenOranges(arr):

    q=deque()
    rotten_oranges=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j]==2):        
                rotten_oranges.append((i,j))
    
    visited=[[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for (start_x,start_y) in rotten_oranges:
        if(visited[start_x][start_y]==0):
            q.append((start_x,start_y,0))
            visited[start_x][start_y]=1
            
    ans=-1
    while(len(q)):
        curr_node=q[0]
        (q.popleft())
        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        for (dir_x,dir_y) in directions:
            new_x=curr_node[0]+dir_x
            new_y=curr_node[1]+dir_y
            if(new_x>=0 and new_x<len(arr) and new_y>=0 and new_y<(len(arr[0]))):                
                if(arr[new_x][new_y]==1 and visited[new_x][new_y]==0):
                    q.append((new_x,new_y,curr_node[2]+1))
                    visited[new_x][new_y]=1
                    ans=max(ans,curr_node[2]+1)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j]==1 and visited[i][j]==0):
                ans=-1
                return ans

    return ans

#rarr=[[0,1,2],[0,1,2],[2,1,1]]
#rarr=[[2, 1, 0, 2, 1],[1, 0, 1, 2, 1],[1, 0, 0, 2, 1]]
rarr=[[2, 1, 0, 2, 1],[0, 0, 1, 2, 1],[1, 0, 0, 2, 1]]
print(RottenOranges(rarr))





    
    