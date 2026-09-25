class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            count[c] = count.get(c, 0) - 1

        for v in count.values():
            if v != 0:
                return False 
        
        return True