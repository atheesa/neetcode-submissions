class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + '#' + s
        print(ans)
        return ans
    
    def decode(self, s: str) -> List[str]:
        ans = []
        while s:
            count = ""
            while s[0] != '#':
                count += s[0]
                s = s[1:]
            print(count)
            count = int(count)
            ans.append(s[1:count + 1])
            s = s[count + 1:]
        return ans