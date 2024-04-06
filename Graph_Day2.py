# Number of Provinces
# Number of Islands
# Flood Fill AAlgorithm
# Rotten Oranges
from collections import deque
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
    
    
    