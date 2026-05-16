class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Input: target = 10, position = [1,4], speed = [3,2]
        # [1,4] [3,2]

        stack = []      

        sorted_ps_zip = sorted(zip(position,speed))

        for i in range(len(sorted_ps_zip)-1,-1,-1):  
            # d/s = t

            curr_time = (target - sorted_ps_zip[i][0]) / sorted_ps_zip[i][1]
            if stack and stack[-1] >= curr_time:
                continue

            stack.append(curr_time)
            
        return len(stack)
        

# 3 seconds
# 10 seconds
# 4.5 seconds
# 3 seconds