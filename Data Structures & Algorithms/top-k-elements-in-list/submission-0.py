class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ows = [[] for i in range(len(nums) + 1) ]

        hashMap = defaultdict(int)
        
        numberSet = set(nums)
        for n in (numberSet):
            cn = nums.count(n)
            ows[cn].append(n)
        
        ans = []
        init = k


        for l in range(len(ows)-1,-1,-1):
            for p in ows[l]:
                if init == 0:
                    return ans
                else:
                    ans.append(p)
                    init -= 1

        return ans
        
        # if init == 0:
        #     return ans
        # else:
            



 