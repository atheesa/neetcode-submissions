class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return

            # dont take value
            dfs(i+1) 

            #take value
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()

        sol, res = [],[]

        dfs(0)
        return res
