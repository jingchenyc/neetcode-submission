class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        m = 1
        for i in range(len(nums) - 1):
            m *= nums[i]
            pre.append(m)
            #1 12 124
        pos = [1]
        n = 1
        for i in range(len(nums) - 1, 0, -1):
            n *= nums[i]
            pos.append(n)
            #6 64 642


        res= []
        for i in range(len(nums)):
            n = len(nums) - 1 - i
            res.append(pre[i] * pos[n])
        return res 