class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
            anagrams = defaultdict(list)
            
            for s in strs:
                # Sort the string and use it as the key
                key = ''.join(sorted(s))
                # Append the original string to the list corresponding to this key
                anagrams[key].append(s)
            
            # Return the grouped anagrams as a list of lists
            return list(anagrams.values())