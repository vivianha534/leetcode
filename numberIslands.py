#https://www.youtube.com/watch?v=pV2kpPD66nE

#Graph algorithim - islands are the vertex
#We start with one cell and check vertically and horizontally for other 1's
#if we see a 1 we check if it's already part of an island, if it is then we don't change the number of islands
#if it isn't then we change the number of islands
#We eventually will visit all of the tiles

#When we first got to the first one, we also want to mark the contiguously adjacent 1's
    #only mark 1's visited once
    #This is a breadth first search
        #doing a graph traversal algorithim starting at og point and marking each layer


class Solution:

    def numIslands(self,grid: List[List[str]]) -> int:
        #if empty grid, return 0
        if not grid:
            return 0
        
        #get dimension of grid
        rows,cols = len(grid), len(grid[0])

        #also want to be able to mark visited cells when marking island masses
        visit = set()
        islands = 0
        
        #bfs is not recursive, it's iterative, so we need a data structure for memory
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            #while q is not empty, we're expanding our island
            while q:
                #want to check adjacent position of the poped tile
                ####if want to do dfs instead of bfs by changing popleft to pop so that it pops most recent element instead of the first element that was added
                    #DFS uses stack, BFS uses queue
                row, col = q.popleft()
                #[[right],[left],[up],[down]]
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                #checks surrounding tiles
                for dr, dc in directions:
                    #checks in bound and it's a 1 and it hasn't been visited yet
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        #add to queue b/c that means we have to run bfs on this cell as well
                        q.append((r,c))
                        #add to visit so we don't visit it twice
                        visit.add((r,c))


        #want to visit every single position in the grid
        for r in range(rows):
            for c in range(cols):
                #we want to increment our islands only if it hasn't been visited yet
                if grid[r][c] == "1" and (r,c) not in visit:
                    #runs traversal
                    bfs(r,c)
                    islands +=1 

        return islands
        