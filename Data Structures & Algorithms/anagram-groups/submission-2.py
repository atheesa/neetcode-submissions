class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we have a lsit of strs, we need a cancoical key to group them, that can be 
        hashMap = defaultdict(list)
        for s in strs:
            s_key = "".join(sorted(s))
            hashMap[s_key].append(s)
        return list(hashMap.values())