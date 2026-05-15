class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):

            while stack and stack[-1][0] < t:
                    val = stack.pop()
                    ans[val[1]] = i - val[1]

            stack.append((t,i))

        return ans

# Input: temperatures = [30,38,28]
# temperature = [30,29,31]
# Output: [1,0,0]   

# [30,29,28,29]