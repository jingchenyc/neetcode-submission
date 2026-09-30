class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = 1
        pos = 1
        for i in range(n):
            res[i] = res[i] * pre
            pre *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * pos
            pos *= nums[i]

        return res
