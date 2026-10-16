class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"]":"[","}":"{",")":"("}
        stack = []
        for br in s:
            if br in matches.values():
                stack.append(br)
            else:
                if stack:
                    br_lhs = stack.pop()
                    if matches[br] != br_lhs:
                        return False
                else:
                    return False
        if stack:
            return False
        return True