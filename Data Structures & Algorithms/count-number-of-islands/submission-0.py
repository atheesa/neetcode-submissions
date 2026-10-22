class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and grid[i][j] == "1":
                    self.ans += 1
                    self.dfs(grid,i,j)
        return self.ans
    
    def dfs(self,grid,i,j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or (i,j) in self.visited or grid[i][j] != "1":
            return
        self.visited.add((i,j))

        self.dfs(grid,i-1,j) 
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        return 
