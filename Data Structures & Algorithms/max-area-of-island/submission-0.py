class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.visited = set()
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (((i,j) not in self.visited)) and grid[i][j] == 1:
                    print(str(i) + ", " + str(j))
                    area = self.dfs(grid,i,j)
                    self.ans = max(self.ans, area)
            
        return self.ans



    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if not ((i,j) in self.visited) and grid[i][j] == 1:
            self.visited.add((i,j))
            return 1 + self.dfs(grid, i-1, j) + self.dfs(grid, i+1, j) + self.dfs(grid, i, j-1) + self.dfs(grid, i, j+1)
        return 0
 