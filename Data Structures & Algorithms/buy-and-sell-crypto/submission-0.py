class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # So you need to a pair of numbers such that the differece between the first index and 
        # and second index is the largest. Well its 2p , so you have a intial index, and while
        # the next value is larger you move the point and at every poin you work out the ans
        # once the point is smaller than the previous you move l to r

        l = 0
        ans = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                ans = max(ans,prices[r] - prices[l])
        return ans