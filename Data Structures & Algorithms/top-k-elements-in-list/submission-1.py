class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # So you are given an array and a k you need to return the k most frequent elements, 
        # So this is a pretty simple heap problem 
        ans = []
        counter = Counter(nums)
        heap = []
        for n, count in counter.items():
            heapq.heappush(heap, (-count, n))

        for _ in range(k):
            neg_count, n = heapq.heappop(heap)
            ans.append(n)
        return ans