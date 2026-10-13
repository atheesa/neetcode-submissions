class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums) + 1)]
        postfix = [1 for _ in range(len(nums) + 1)]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] * prefix[i]

        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]

        for i in range(len(nums)):
            ans[i] = prefix[i] * postfix[i + 1]
        return ans