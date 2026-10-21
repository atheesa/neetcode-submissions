class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     # string only 26 chars , int k, replace k with an other letter,
     # sliding window -> and we need to count either the max char so you need to 
     # a way of maintaing the the largest letter
     # hashmap -> 

        counter = defaultdict(int)
        max_char_count = 0
        l = 0
        res = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            max_char_count = max(counter[s[r]], max_char_count)

            while( ((r-l)+1) - max_char_count > k):
                counter[s[l]] -= 1
                l += 1
                max_char_count = max(counter[s[l]], max_char_count)
            
            res = (r - l) + 1
        return res
