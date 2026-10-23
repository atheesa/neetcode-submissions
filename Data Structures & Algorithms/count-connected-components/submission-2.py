class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for e in adj[n]:
                dfs(e)
            return
        visited = set()
        ans = 0 
        adj = defaultdict(list)

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i) 
        return ans