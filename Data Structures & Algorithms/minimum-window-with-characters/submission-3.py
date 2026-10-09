class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        bestStart = 0
        bestLen = float("inf")

        for c in t:
            target[c] = target.get(c, 0) + 1

        match = len(t)

        l = 0
        for r in range(len(s)):
            target[s[r]] = target.get(s[r], 0) - 1
            if target[s[r]] >= 0:
                match -= 1
            
            while match == 0:
                if r - l + 1 < bestLen:
                    bestLen = r - l + 1
                    bestStart = l

                target[s[l]] += 1
                if target[s[l]] - 1 == 0:
                    match += 1
                l += 1

            
        if bestLen == float("inf"):
            return ""
        
        return s[bestStart:bestStart + bestLen]