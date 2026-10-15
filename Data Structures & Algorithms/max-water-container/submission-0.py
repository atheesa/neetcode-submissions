class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # So we are given a array of with heights, 
        # What is the problem 
        # are given a a list of hightes and we need to work out for a pair what the largest area of 
        # of water that can fit in between 2 pairs well we need to figure out for each bar whats the largest amount of water
        # well for a given point lets see how much water it can hold well, this thought chain is halted
        # lets look at another approach, if we have l r and we just move the smaller height we can 
        # come up with the solution , the key is to think about the equation a = h x w, we maximise w at the start
        # and we are now just trying to maximise h as much as possible
        

        l, r = 0, len(heights) - 1
        area = 0
        while (l < r):
            area = max(area, min(heights[l],heights[r]) * (r - l))
            if(heights[l] > heights[r]):
                r-=1
            else:
                l+=1
        return area
