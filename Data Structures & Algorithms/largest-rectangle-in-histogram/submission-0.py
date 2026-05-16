class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pre_compute = [0] * len(heights)
        for r in range(len(heights)):
            ll = r  
            lr = r
            while(ll > 0 and heights[ll - 1] >= heights[r]):
                ll -= 1

            while(lr < len(heights) - 1 and heights[lr + 1] >= heights[r]):
                lr += 1
            pre_compute[r] = lr - ll + 1
        
        ans = max([heights[i] * pre_compute[i] for i in range(len(heights))])
        return ans

