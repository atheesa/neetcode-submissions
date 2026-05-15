class Solution:

    
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s 
        return encodedStr

    def decode(self, s: str) -> List[str]:
        
        #       4#neet4#code
        i = 0
        ans = []

        while i < len(s):
            j = i
            numStr = ""
            while (s[j] != '#'):
                numStr += s[j]
                j += 1
            
            numInt = int(numStr)
            tempStr = s[j+1:j+1+numInt]
            ans.append(tempStr)
            i = j+1+numInt
        
        return ans


