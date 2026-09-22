class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        R,C=len(grid),len(grid[0])
        area=0
        def bfs(r,c):
            q=deque()
            res=1
            grid[r][c]=0
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in dir:
                    nr,nc=row+dr,col+dc
                    if(nr<0 or nc<0 or nr>=R or nc>=C or grid[nr][nc]==0):
                        continue
                    res+=1
                    q.append((nr,nc))
                    grid[nr][nc]=0
            return res
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    area=max(area,bfs(r,c))
        return area