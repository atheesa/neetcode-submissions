class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        comp = 0
        def dfs(i):
            visited.add(i)
            for neighbour in graph[i]:
                if neighbour not in visited:
                    dfs(neighbour)
            return
        
        for i in range(n):
            if i not in visited:
                comp += 1
                dfs(i)
        return comp
            
