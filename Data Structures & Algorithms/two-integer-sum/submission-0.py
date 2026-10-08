class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # So you are given an array of numbers and you need to get 2 numbers that add to the target
        # you can go through the array and check if the
        seen = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in seen:
                return [seen[needed], i]
            seen[n] = i
        return [-1,-1] 