class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        f=0
        q=collections.deque()
        t=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    f+=1
                if grid[r][c]==2:
                    q.append((r,c))
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        while f>0 and q:
            l=len(q)
            for i in range(l):
                r, c=q.popleft()

               
                for dr,dc in dir:
                    row,col=r+dr,c+dc
                    if(row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row,col))
                        f-=1
            t+=1
        return t if f==0 else -1
                    
