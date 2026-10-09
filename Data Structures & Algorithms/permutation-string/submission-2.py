class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        window = [0] * 26
        target = [0] * 26

        for i in range(m) :
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if target == window:
            return True

        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - m]) - ord('a')] -= 1
            
            if target == window:
                return True

        return False
        