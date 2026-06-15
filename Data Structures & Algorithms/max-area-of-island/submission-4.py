class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxLand = 0
        visited = set()
        rows, cols = len(grid),len(grid[0])
        q = collections.deque()

        def bfs(r,c):
            area = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            q.append((r,c))
            visited.add((r,c))
            while q :
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and
                    grid[r][c] == 1 and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        area+=1
            return area
        for r in range(rows) :
            for c in range(cols):
                if grid[r][c] ==1:
                    maxLand = max(bfs(r,c),maxLand)
        return maxLand