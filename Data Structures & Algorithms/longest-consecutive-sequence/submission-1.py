class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for n in nums:
            l_n = n
            l_ans = 1
            if (l_n - 1) not in nums_set:
                while(l_n + 1) in nums_set:
                    l_ans += 1
                    l_n += 1
            ans = max(ans,l_ans)
        return ans
