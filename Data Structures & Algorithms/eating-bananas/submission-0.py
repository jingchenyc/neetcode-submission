class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            s = (l + r) // 2
            maxT = 0
            for p in piles:
                maxT += math.ceil(float(p) / s)
            if maxT <= h:
                res = s
                r = s - 1
            else:
                l = s + 1
        
        return res
             