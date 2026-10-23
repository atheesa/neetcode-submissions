class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # So what is happening here we need to create a adj list and then we need to 
        # find a cycle -> cycle usual pattern. visiting -> visited
        courses = prerequisites
        self.edges = defaultdict(list)

        for i,a in courses:
            self.edges[i].append(a)
        
        self.visiting = set()
        self.visited = set()
    
        for i in range((numCourses)):
            if not self.dfs(i):
                return False
        
        return True


    # return no loop? ((true) bool)
    def dfs(self, node):
        if node in self.visited:
            return True
        if node in self.visiting:
            return False

        self.visiting.add(node)
        for e in self.edges[node]:
            if not self.dfs(e):
                return False
        self.visiting.remove(node)
        self.visited.add(node)

        return True
            