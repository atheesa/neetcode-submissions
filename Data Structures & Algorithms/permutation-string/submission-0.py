class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = Counter(s1)
        s2_set = Counter(s2[:len(s1)])
        if s1_set == s2_set:
                return True
            
        # So you would have like s1 = ""abc"", s2 = "lecaabee" -> abc lec
        for r in range(len(s1), len(s2)):
            # 3
            # 4-1 (3)
            print(s1_set)
            print(s2_set)
            print("-------")
            s2_set[(s2[(r - len(s1))])] -= 1
            s2_set[(s2[r])] += 1
            if s1_set == s2_set:
                return True

        return False